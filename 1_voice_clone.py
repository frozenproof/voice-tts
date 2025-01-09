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
import pandas as pd

warnings.filterwarnings("ignore", category=FutureWarning)
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True

def get_timestamp():
    return datetime.utcnow().strftime('%Y%m%d_%H%M%S')

class VoiceConverter:
    def __init__(self, ckpt_converter, device, output_dir):
        self.ckpt_converter = ckpt_converter
        self.device = device
        self.output_dir = output_dir
        self.speaker_embedding_cache = {}
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
        
    def process_text(self, text, language_key, reference_speaker, language='EN', speed=1.0):
        try:
            torch.set_float32_matmul_precision('high')
            
            # Cache for TTS models
            if not hasattr(self, 'tts_model_cache'):
                self.tts_model_cache = {}
                
            if language not in self.tts_model_cache:
                self.tts_model_cache[language] = TTS(language=language, device=self.device)
            
            model = self.tts_model_cache[language]
            speaker_ids = model.hps.data.spk2id
            print("All available speaker keys id", speaker_ids.keys())
            
            print(f"Processing reference audio: {reference_speaker}")
            if not hasattr(self, 'target_se_cache'):
                self.target_se_cache = {}
                
            if reference_speaker not in self.target_se_cache:
                target_se, _ = se_extractor.get_se(reference_speaker, self.tone_color_converter, vad=True)
                self.target_se_cache[reference_speaker] = target_se
            target_se = self.target_se_cache[reference_speaker]
            
            timestamp = get_timestamp()
            src_path = f'{self.output_dir}/tmp_{timestamp}.wav'

            # For EN_NEWEST, use EN-Newest directly
            if language == 'EN_NEWEST' and 'EN-Newest' in speaker_ids:
                matching_speaker = 'EN-Newest'
            else:
                # Original matching logic for other cases
                normalized_input = language_key.upper().replace('-', '_')
                matching_speaker = None
                for speaker_key in speaker_ids.keys():
                    if speaker_key == normalized_input or speaker_key.replace('_', '-') == language_key.upper():
                        matching_speaker = speaker_key
                        break

            if not matching_speaker:
                print(f"No matching speaker found for {language_key}. Available speakers: {list(speaker_ids.keys())}")
                return
            
            speaker_id = speaker_ids[matching_speaker]
            normalized_key = matching_speaker.lower().replace('_', '-')
            
            try:
                print(f"Processing speaker: {normalized_key}")
                source_se_path = f'checkpoints_v2/base_speakers/ses/{normalized_key}.pth'
                
                if not os.path.exists(source_se_path):
                    print(f"Warning: Speaker embedding file not found at {source_se_path}")
                    return
                
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
                    f'output_v2_{normalized_key}_{timestamp}_{safe_text}_{language}.wav'
                )
                
                print(f"Converting voice style...")
                self.tone_color_converter.convert(
                    audio_src_path=src_path,
                    src_se=source_se,
                    tgt_se=target_se,
                    output_path=save_path
                )
                print(f"Saved output to: {save_path}")
                
            except Exception as e:
                print(f"Error processing speaker {normalized_key}: {str(e)}")
                
            if os.path.exists(src_path):
                os.remove(src_path)
                
        except Exception as e:
            print(f"Error in process_text: {str(e)}")
            raise

def load_texts_from_excel(excels):
    """
    Load texts from multiple Excel files and convert to the format needed for processing
    Expected Excel format:
    | language | speaker_key | text_content |
    | EN      | EN-US       | Some text... |
    | EN      | EN-BR       | Some text... |
    | ZH      | EN-Default  | Some text... |
    """
    all_texts = {}
    
    for category, excel_files in excels.items():
        for excel_info in excel_files:
            file_path = Path(*excel_info["path"])
            
            try:
                df = pd.read_excel(file_path)
                
                # Verify required columns exist
                required_cols = ['language', 'speaker_key', 'text_content']
                if not all(col in df.columns for col in required_cols):
                    print(f"Warning: Excel file {file_path} missing required columns: {required_cols}")
                    continue
                
                # Create a dictionary with tuple keys (language, speaker_key)
                texts_from_excel = {
                    row['speaker_key']: {
                        'text': row['text_content'],
                        'language': row['language']
                    }
                    for _, row in df.iterrows()
                }
                
                # Update the main texts dictionary
                all_texts.update(texts_from_excel)
                
            except Exception as e:
                print(f"Error reading Excel file {file_path}: {str(e)}")
                continue
    
    return all_texts

def main():
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    converter = VoiceConverter(
        ckpt_converter='checkpoints_v2/converter',
        device=device,
        output_dir='outputs_v2'
    )
    
    # Define excel files to process
    # Define excel files to process
    excels = {
        "key1": [
            {"path": ["voices_input", "file1.xlsx"]}
        ],
        # "key2": [
        #     {"path": ["voices_input", "file3.xlsx"]},
        #     {"path": ["voices_input", "file4.xlsx"]}
        # ]
    }
    
    # Use the correct speaker keys that match the model's speaker_ids
    # texts = {
    #     'EN_INDIA': "I'm going to say. First of all I want you to love yourself, which I know is impossible because you are a goth.",
    #     'EN-BR': "I'm going to say. First of all I want you to love yourself, which I know is impossible because you are a goth.",
    # }
    
    # Load texts from Excel files
    texts = load_texts_from_excel(excels)
    reference_speaker = 'resources/demo_speaker1.mp3'
    
    # Group texts by language to minimize model reloading
    texts_by_language = {}
    for speaker_key, info in texts.items():
        language = info['language']
        if language not in texts_by_language:
            texts_by_language[language] = []
        texts_by_language[language].append((speaker_key, info))
    
    print("\nStarting voice conversion process...")
    # Process each language group
    for language, text_group in texts_by_language.items():
        print(f"\nProcessing language: {language}")
        for speaker_key, info in text_group:
            try:
                print(f"\nProcessing text: {info['text']}")
                converter.process_text(
                    text=info['text'],
                    language_key=speaker_key,
                    reference_speaker=reference_speaker,
                    language=language
                )
                print("Processing completed successfully")
            except Exception as e:
                print(f"Error processing text '{info['text']}': {str(e)}")
                continue

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Fatal error: {str(e)}")