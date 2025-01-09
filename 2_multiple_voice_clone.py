import os
import torch
import requests
import zipfile
import shutil
import warnings
from datetime import datetime
from pathlib import Path
from openvoice import se_extractor
from openvoice.api import ToneColorConverter
from melo.api import TTS

warnings.filterwarnings("ignore", category=FutureWarning)
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True

def get_timestamp():
    """Generate a timestamp for filenames"""
    return datetime.utcnow().strftime('%Y%m%d_%H%M%S')

class VoiceConverter:
    def __init__(self, ckpt_converter, device, output_dir):
        self.ckpt_converter = ckpt_converter
        self.device = device
        self.output_dir = output_dir
        self.speaker_embedding_cache = {}  # Fixed: Added cache initialization
        print(f"Initializing VoiceConverter on device: {self.device}")
        self.setup_converter()
        
    def setup_converter(self):
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        
        self.tone_color_converter = ToneColorConverter(
            f'{self.ckpt_converter}/config.json', 
            device=self.device
        )
        self.tone_color_converter.load_ckpt(f'{self.ckpt_converter}/checkpoint.pth')
        os.makedirs(self.output_dir, exist_ok=True)
        
    def process_text(self, text, language_prefix, reference_speaker, speed=1.0):
        try:
            torch.set_float32_matmul_precision('high')
            model = TTS(language=language_prefix, device=self.device)
            speaker_ids = model.hps.data.spk2id
            
            matching_speakers = {
                key: speaker_ids[key] 
                for key in speaker_ids.keys() 
                if key.lower().startswith(language_prefix.lower())
            }
            
            if not matching_speakers:
                print(f"No speakers found matching prefix: {language_prefix}")
                return
                
            print(f"Found {len(matching_speakers)} matching speakers: {list(matching_speakers.keys())}")
            
            print(f"Processing reference audio: {reference_speaker}")
            target_se, _ = se_extractor.get_se(reference_speaker, self.tone_color_converter, vad=True)
            
            timestamp = get_timestamp()
            src_path = f'{self.output_dir}/tmp_{timestamp}.wav'
            
            for speaker_key, speaker_id in matching_speakers.items():
                try:
                    normalized_key = speaker_key.lower().replace('_', '-')
                    print(f"Processing speaker: {normalized_key}")
                    
                    source_se_path = f'checkpoints_v2/base_speakers/ses/{normalized_key}.pth'
                    if not os.path.exists(source_se_path):
                        print(f"Warning: Speaker embedding not found for {normalized_key}")
                        continue
                    
                    if normalized_key in self.speaker_embedding_cache:
                        source_se = self.speaker_embedding_cache[normalized_key]
                    else:
                        source_se = torch.load(source_se_path, map_location=self.device)
                        self.speaker_embedding_cache[normalized_key] = source_se
                    
                    print(f"Generating TTS audio for text: {text}")
                    model.tts_to_file(text, speaker_id, src_path, speed=speed)
                    
                    safe_text = "".join(x for x in text[:30] if x.isalnum() or x in (' ', '_', '-'))
                    save_path = os.path.join(
                        self.output_dir, 
                        f'output_v2_{normalized_key}_{timestamp}_{safe_text}.wav'
                    )
                    
                    print(f"Converting voice style...")
                    torch.cuda.synchronize()
                    self.tone_color_converter.convert(
                        audio_src_path=src_path,
                        src_se=source_se,
                        tgt_se=target_se,
                        output_path=save_path
                    )
                    print(f"Saved output to: {save_path}")
                    
                    torch.cuda.empty_cache()
                    
                except Exception as e:
                    print(f"Error processing speaker {normalized_key}: {str(e)}")
                    continue
                    
            if os.path.exists(src_path):
                os.remove(src_path)
                
        except Exception as e:
            print(f"Error in process_text: {str(e)}")
            raise

def main():
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    converter = VoiceConverter(
        ckpt_converter='checkpoints_v2/converter',
        device=device,
        output_dir='outputs_v2'
    )
    
    texts = {
        'EN': "",  # Start with a simple test
    }
    
    reference_speaker = 'resources/demo_speaker1.mp3'
    
    print("\nStarting voice conversion process...")
    for language_prefix, text in texts.items():
        try:
            print(f"\nProcessing text: {text}")
            converter.process_text(text, language_prefix, reference_speaker)
            print("Processing completed successfully")
        except Exception as e:
            print(f"Error processing text '{text}': {str(e)}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Fatal error: {str(e)}")