
# Chatgpt version

# Hệ Thống Chấm Điểm An Toàn Thông Tin Cho Microservices

Hệ thống chấm điểm này dựa trên các tiêu chuẩn quốc tế như **ISO/IEC 27001**, **NIST SP 800-53**, và **OWASP Microservices Security**. Tổng điểm là **200**, chia thành hai phần chính: **Cơ sở hạ tầng Microservices (100 điểm)** và **Ứng dụng Microservices (100 điểm)**.

---

## 1. Hướng Dẫn Chấm Điểm Chung
- **0 điểm**: Không triển khai.
- **1 điểm**: Triển khai cơ bản nhưng không đầy đủ.
- **2 điểm**: Triển khai nhưng chưa kiểm tra thường xuyên.
- **3 điểm**: Triển khai đầy đủ, kiểm tra định kỳ.
- **4 điểm**: Triển khai tối ưu, cải tiến liên tục.

---

## 2. Phần A: Cơ Sở Hạ Tầng Microservices (100 điểm)
| **Tiêu Chí**                 | **Mô Tả**                                                                                  | **Điểm Tối Đa** | **Hướng Dẫn Chấm**                                                                                   | **Tài Liệu Tham Khảo**                                                       |
|-----------------------------|------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **1. Bảo mật API**           |                                                                                          |                |                                                                                                     |                                                                            |
| - Xác thực API               | Sử dụng OAuth 2.0 hoặc OpenID Connect.                                                   | 4              | 0 nếu không có xác thực; 4 nếu sử dụng tiêu chuẩn mạnh.                                              | NIST SP 800-204: Section 3.4, OWASP Microservices Security Cheat Sheet: Authentication |
| - Mã hóa truyền tải          | Mọi giao tiếp API đều dùng HTTPS/TLS.                                                   | 4              | 0 nếu không mã hóa; 4 nếu tất cả giao tiếp đều được mã hóa.                                         | NIST SP 800-204: Section 3.5, OWASP Microservices Security Cheat Sheet: Data in Transit |
| - Giới hạn tốc độ truy cập   | Sử dụng rate limiting hoặc throttling để chống DDoS.                                     | 4              | 0 nếu không có cơ chế; 4 nếu triển khai tự động.                                                    | NIST SP 800-204: Section 3.2, OWASP Microservices Security Cheat Sheet: Rate Limiting |
| - Kiểm tra đầu vào           | Xác thực và làm sạch dữ liệu đầu vào để chống tấn công (SQLi, XSS).                       | 4              | 0 nếu không kiểm tra; 4 nếu kiểm tra đầy đủ và định kỳ.                                             | NIST SP 800-204: Section 3.6, OWASP Microservices Security Cheat Sheet: Input Validation |
| **2. Bảo vệ dữ liệu**         |                                                                                          |                |                                                                                                     |                                                                            |
| - Mã hóa dữ liệu lưu trữ     | Sử dụng AES-256 hoặc tương đương cho dữ liệu nhạy cảm.                                   | 4              | 0 nếu không mã hóa; 4 nếu mọi dữ liệu quan trọng đều mã hóa.                                        | NIST SP 800-204: Section 3.5, CIS Docker Benchmark: Section 6.2.2 |
| - Sao lưu và khôi phục       | Sao lưu tự động và kiểm tra khôi phục thường xuyên.                                      | 4              | 0 nếu không sao lưu; 4 nếu kiểm tra định kỳ và đảm bảo an toàn.                                     | NIST SP 800-204: Section 3.3                                                              |
| **3. Quản lý cấu hình**       |                                                                                          |                |                                                                                                     |                                                                            |
| - Công cụ quản lý cấu hình   | Sử dụng Terraform, Ansible hoặc công cụ tự động khác.                                    | 4              | 0 nếu cấu hình thủ công; 4 nếu cấu hình được tự động hóa hoàn toàn.                                | NIST SP 800-204: Section 4.2, CIS Docker Benchmark: Section 2.4 |
| - Kiểm tra cấu hình định kỳ  | Đánh giá cấu hình dựa trên tiêu chuẩn CIS.                                               | 4              | 0 nếu không kiểm tra; 4 nếu có lịch trình kiểm tra định kỳ.                                         | CIS Docker Benchmark: Section 2.5                                                    |
| **4. An ninh mạng**           |                                                                                          |                |                                                                                                     |                                                                            |
| - Phân đoạn mạng             | Sử dụng chính sách phân đoạn mạng để cô lập microservices quan trọng.                   | 4              | 0 nếu không có phân đoạn; 4 nếu áp dụng phân đoạn toàn diện.                                       | OWASP Microservices Security Cheat Sheet: Network Segmentation |
| - Sử dụng giao thức bảo mật  | Giao tiếp giữa microservices dùng mTLS hoặc tương đương.                                | 4              | 0 nếu không có giao thức bảo mật; 4 nếu mọi giao tiếp đều bảo mật.                                 | NIST SP 800-204: Section 3.5, OWASP Microservices Security Cheat Sheet: Secure Communication |
| **5. Giám sát và nhật ký**    |                                                                                          |                |                                                                                                     |                                                                            |
| - Ghi nhật ký sự kiện an ninh| Ghi nhận đầy đủ và lưu trữ tập trung các sự kiện quan trọng.                             | 4              | 0 nếu không có hoặc thiếu sót; 4 nếu ghi nhật ký đầy đủ và theo dõi thường xuyên.                   | NIST SP 800-204: Section 4.1, OWASP Microservices Security Cheat Sheet: Logging |
| - Cảnh báo bất thường        | Tự động gửi cảnh báo khi phát hiện hành vi bất thường.                                  | 4              | 0 nếu không có cơ chế cảnh báo; 4 nếu tích hợp với công cụ như Prometheus hoặc ELK.                 | OWASP Microservices Security Cheat Sheet: Anomaly Detection |
| - Phân tích nhật ký          | Sử dụng công cụ phân tích để tìm kiếm các mối đe dọa.                                   | 4              | 0 nếu không phân tích; 4 nếu phân tích nhật ký thường xuyên và chi tiết.                           | NIST SP 800-204: Section 4.1                                                              |
| - Kiểm tra bảo mật tự động   | Tích hợp kiểm tra bảo mật tự động trong quy trình CI/CD.                                | 4              | 0 nếu không kiểm tra; 4 nếu kiểm tra đầy đủ trong mọi lần triển khai.                              | NIST SP 800-204: Section 5.2                                                             |
| - Quản lý lỗ hổng            | Sử dụng công cụ để phát hiện và quản lý các lỗ hổng trong hệ thống.                     | 4              | 0 nếu không có công cụ; 4 nếu có quy trình xử lý và giám sát liên tục.                             | NIST SP 800-204: Section 3.7, CIS Docker Benchmark: Section 5.4 |
| - Bảo mật lưu trữ container  | Container được cấu hình để ngăn chặn ghi đè không được phép.                            | 4              | 0 nếu không có cơ chế; 4 nếu thực hiện đầy đủ.                                                     | CIS Docker Benchmark: Section 6.2.5, OWASP Microservices Security Cheat Sheet: Container Security |
| - Quản lý bí mật             | Sử dụng Vault hoặc Secret Manager cho thông tin nhạy cảm.                               | 4              | 0 nếu không có công cụ; 4 nếu triển khai đầy đủ.                                                   | NIST SP 800-204: Section 3.4                                                              |
| - Chính sách danh sách trắng IP | Giới hạn truy cập mạng chỉ từ IP được phê duyệt.                                       | 4              | 0 nếu không thực hiện; 4 nếu áp dụng toàn diện.                                                    | NIST SP 800-204: Section 3.8                                                              |
| - Hệ thống phát hiện xâm nhập (IDS) | Triển khai IDS để giám sát hoạt động bất thường.                                   | 4              | 0 nếu không có; 4 nếu tích hợp với hệ thống báo cáo sự cố.                                         | NIST SP 800-204: Section 4.3                                                             |
| - Đăng nhập không đặc quyền  | Không cho phép tài khoản root hoặc admin đăng nhập trực tiếp.                           | 4              | 0 nếu không có biện pháp; 4 nếu áp dụng đầy đủ.                                                    | NIST SP 800-204: Section 3.3, CIS Docker Benchmark: Section 6.4 |
| - Cô lập dữ liệu             | Cô lập hoàn toàn dữ liệu ứng dụng khỏi hệ điều hành container.                          | 4              | 0 nếu không thực hiện; 4 nếu đảm bảo cô lập hoàn toàn.                                             | CIS Docker Benchmark: Section 6.6                                                    |
| - Bảo vệ host                | Sử dụng công cụ như Falco để phát hiện hành vi đáng ngờ trong host.                     | 4              | 0 nếu không áp dụng; 4 nếu tích hợp và giám sát đầy đủ.                                            | NIST SP 800-204: Section 4.4                                                              |
| - Chính sách quản lý ảnh container | Quét và xác minh chữ ký trước khi sử dụng ảnh container.                            | 4              | 0 nếu không quét; 4 nếu áp dụng đầy đủ.                                                            | CIS Docker Benchmark: Section 6.3                                                    |
| - Phân đoạn VLAN             | Cách ly microservices trong các VLAN khác nhau.                                         | 4              | 0 nếu không cách ly; 4 nếu áp dụng đầy đủ.                                                         | NIST SP 800-204: Section 3.9                                                              |

---

## 3. Phần B: Ứng Dụng Microservices (100 điểm)

| **Tiêu Chí**                        | **Mô Tả**                                                                                     | **Điểm Tối Đa** | **Hướng Dẫn Chấm**                                                                                   | **Tài Liệu Tham Khảo**                                                       |
|-------------------------------------|----------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **1. Thiết kế dịch vụ**              |                                                                                              |                |                                                                                                     |                                                                            |
| - Tách biệt trách nhiệm             | Mỗi microservice đảm nhận một nhiệm vụ cụ thể (Single Responsibility Principle).             | 4              | 0 nếu nhiệm vụ chồng chéo; 4 nếu rõ ràng, độc lập.                                                  | NIST SP 800-204: Section 3.4                                                  |
| - Tự phục hồi                      | Microservices có khả năng tự phục hồi khi gặp lỗi.                                           | 4              | 0 nếu phụ thuộc hoàn toàn vào hệ thống bên ngoài; 4 nếu tự phục hồi được.                          | NIST SP 800-204: Section 3.3                                                  |
| - Phân tách dữ liệu                 | Mỗi dịch vụ có cơ sở dữ liệu riêng, không chia sẻ schema.                                    | 4              | 0 nếu dùng chung; 4 nếu tách biệt hoàn toàn.                                                       | NIST SP 800-204: Section 4.1                                                  |
| **2. Bảo mật ứng dụng**              |                                                                                              |                |                                                                                                     |                                                                            |
| - Mã hóa thông tin nhạy cảm        | Mọi thông tin nhạy cảm đều được mã hóa trước khi xử lý.                                       | 4              | 0 nếu không mã hóa; 4 nếu mọi thông tin nhạy cảm đều được bảo mật.                                 | NIST SP 800-204: Section 3.5                                                  |
| - Chính sách truy cập              | Áp dụng nguyên tắc tối thiểu quyền (Least Privilege).                                        | 4              | 0 nếu quyền không được quản lý; 4 nếu có chính sách kiểm soát rõ ràng.                             | OWASP Microservices Security Cheat Sheet: Least Privilege                   |
| - Bảo mật đầu vào                   | Kiểm tra và làm sạch mọi dữ liệu đầu vào từ người dùng.                                      | 4              | 0 nếu không kiểm tra; 4 nếu kiểm tra đầy đủ và thường xuyên.                                       | OWASP Microservices Security Cheat Sheet: Input Validation                  |
| **3. Đảm bảo chất lượng**            |                                                                                              |                |                                                                                                     |                                                                            |
| - Kiểm thử định kỳ                 | Mọi microservices được kiểm thử định kỳ với các bộ công cụ tự động.                          | 4              | 0 nếu không kiểm thử; 4 nếu kiểm thử toàn diện và tự động hóa.                                      | NIST SP 800-204: Section 5.2                                                  |
| - Giám sát hiệu suất               | Sử dụng APM (Application Performance Monitoring) để theo dõi hiệu suất.                       | 4              | 0 nếu không có công cụ APM; 4 nếu tích hợp công cụ giám sát hiệu suất.                             | NIST SP 800-204: Section 5.1                                                  |
| - Đo lường độ trễ                  | Theo dõi và tối ưu độ trễ giữa các dịch vụ.                                                  | 4              | 0 nếu không đo lường; 4 nếu có hệ thống đo và cải thiện.                                           | NIST SP 800-204: Section 5.3                                                  |
| - Kiểm tra tải                     | Thực hiện kiểm tra tải để đảm bảo hiệu suất dưới áp lực.                                     | 4              | 0 nếu không kiểm tra; 4 nếu có kiểm tra định kỳ và cải tiến hiệu suất.                             | NIST SP 800-204: Section 5.4                                                  |
| **4. Bảo mật bổ sung**              |                                                                                              |                |                                                                                                     |                                                                            |
| - Kiểm soát session                | Hết hiệu lực session tự động sau một thời gian không hoạt động.                              | 4              | 0 nếu không áp dụng; 4 nếu có cơ chế hết hiệu lực tự động.                                          | OWASP Microservices Security Cheat Sheet: Session Management                |
| - Bảo vệ chống CSRF                | Sử dụng mã thông báo CSRF trong các yêu cầu trạng thái.                                      | 4              | 0 nếu không sử dụng mã thông báo CSRF; 4 nếu sử dụng hiệu quả.                                      | OWASP Microservices Security Cheat Sheet: CSRF Protection                   |
| - Cảnh báo thất bại đăng nhập      | Gửi cảnh báo khi có nhiều lần đăng nhập thất bại.                                            | 4              | 0 nếu không có cảnh báo; 4 nếu có hệ thống cảnh báo đầy đủ.                                          | NIST SP 800-204: Section 3.2                                                  |
| - Tự động kiểm tra đầu cuối        | Tích hợp kiểm tra E2E cho các lỗ hổng bảo mật.                                               | 4              | 0 nếu không có kiểm tra; 4 nếu có kiểm tra bảo mật E2E tự động.                                     | NIST SP 800-204: Section 5.1                                                  |
| - Chính sách lưu trữ log           | Mã hóa log và chỉ giữ dữ liệu trong thời gian quy định.                                      | 4              | 0 nếu không mã hóa hoặc lưu trữ lâu dài; 4 nếu mã hóa và lưu trữ có hạn.                           | NIST SP 800-204: Section 4.1, OWASP Microservices Security Cheat Sheet: Logging |
| - Xử lý lỗi an toàn                | Không tiết lộ thông tin nhạy cảm qua thông báo lỗi.                                           | 4              | 0 nếu thông báo lỗi chứa thông tin nhạy cảm; 4 nếu bảo vệ thông tin nhạy cảm trong thông báo lỗi.  | NIST SP 800-204: Section 3.6                                                  |
| - Đánh giá bảo mật API            | Tích hợp công cụ API Gateway với bảo mật mở rộng.                                            | 4              | 0 nếu không tích hợp bảo mật; 4 nếu tích hợp đầy đủ API Gateway với bảo mật mở rộng.              | NIST SP 800-204: Section 3.7                                                  |
| - Kiểm tra thường xuyên với OWASP ZAP | Sử dụng OWASP ZAP để kiểm tra các endpoint.                                               | 4              | 0 nếu không sử dụng OWASP ZAP; 4 nếu kiểm tra đầy đủ các endpoint với OWASP ZAP.                   | OWASP Microservices Security Cheat Sheet: Vulnerability Scanning             |
| - Theo dõi các sự kiện chuỗi cung ứng | Xác minh nguồn gốc thư viện và module bên thứ ba.                                          | 4              | 0 nếu không kiểm tra; 4 nếu có hệ thống xác minh nguồn gốc của tất cả thư viện và module.          | NIST SP 800-204: Section 3.8                                                  |
| - Phát hiện sự khác biệt trong hành vi API | Sử dụng AI để phát hiện hành vi không mong muốn.                                           | 4              | 0 nếu không sử dụng AI; 4 nếu có hệ thống AI để phát hiện hành vi không mong muốn.                | NIST SP 800-204: Section 3.9                                                  |
| - Tích hợp đa yếu tố xác thực (MFA) | Sử dụng MFA cho tất cả các endpoint quản trị.                                               | 4              | 0 nếu không áp dụng MFA; 4 nếu áp dụng MFA cho tất cả endpoint quản trị.                            | NIST SP 800-204: Section 3.4                                                  |
| - Phân tích tác động bảo mật của CI/CD | Kiểm tra pipeline CI/CD cho lỗ hổng.                                                        | 4              | 0 nếu không kiểm tra; 4 nếu có kiểm tra pipeline CI/CD định kỳ.                                     | NIST SP 800-204: Section 5.2                                                  |
| - Phân tích hành vi người dùng (UEBA) | Giám sát hành vi và phát hiện sự bất thường.                                               | 4              | 0 nếu không giám sát hành vi người dùng; 4 nếu giám sát và phát hiện bất thường hiệu quả.           | NIST SP 800-204: Section 4.3                                                  |
| - Đánh giá quyền truy cập đối với nhân viên | Xem xét quyền truy cập định kỳ.                                                           | 4              | 0 nếu không đánh giá; 4 nếu có đánh giá định kỳ và cập nhật quyền truy cập.                        | NIST SP 800-204: Section 3.4                                                  |
| - Kiểm thử bảo mật giả lập         | Tổ chức các bài kiểm thử giả lập tấn công (Red Team).                                       | 4              | 0 nếu không có kiểm thử; 4 nếu có kiểm thử giả lập tấn công định kỳ.                                | NIST SP 800-204: Section 4.4                                                  |


## **4. Tổng điểm và đánh giá**

| **Tổng Điểm** | **Xếp Loại An Toàn**          |
|---------------|-------------------------------|
| **90-100**    | An toàn cao (Đáp ứng tốt)     |
| **75-89**     | Tương đối an toàn (Đáp ứng)   |
| **50-74**     | Trung bình (Cần cải thiện)    |
| **<50**       | Nguy cơ cao (Cần khắc phục ngay) |

## **5. Tài liệu tham khảo**
- **NIST SP 800-204**: [Link](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204.pdf)  
- **CIS Docker Benchmark**: [Link](https://www.cisecurity.org/benchmark/docker)  
- **OWASP Microservices Security Cheat Sheet**: [Link](https://cheatsheetseries.owasp.org/cheatsheets/Microservices_Security_Cheat_Sheet.html)


# Base
# Hệ Thống Chấm Điểm An Toàn Thông Tin Cho Microservices

Hệ thống chấm điểm này dựa trên các tiêu chuẩn quốc tế như **ISO/IEC 27001**, **NIST SP 800-53**, và **OWASP Microservices Security**. Tổng điểm là **200**, chia thành hai phần chính: **Cơ sở hạ tầng Microservices (100 điểm)** và **Ứng dụng Microservices (100 điểm)**.

---

## 1. Hướng Dẫn Chấm Điểm Chung
- **0 điểm**: Không triển khai.
- **1 điểm**: Triển khai cơ bản nhưng không đầy đủ.
- **2 điểm**: Triển khai nhưng chưa kiểm tra thường xuyên.
- **3 điểm**: Triển khai đầy đủ, kiểm tra định kỳ.
- **4 điểm**: Triển khai tối ưu, cải tiến liên tục.

---

## 2. Phần A: Cơ Sở Hạ Tầng Microservices (100 điểm)

| **Tiêu Chí**                 | **Mô Tả**                                                                                  | **Điểm Tối Đa** | **Hướng Dẫn Chấm**                                                                                   |
|-----------------------------|------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| **1. Bảo mật API**           |                                                                                          |                |                                                                                                     |
| - Xác thực API               | Sử dụng OAuth 2.0 hoặc OpenID Connect.                                                   | 4              | 0 nếu không có xác thực; 4 nếu sử dụng tiêu chuẩn mạnh.                                              |
| - Mã hóa truyền tải          | Mọi giao tiếp API đều dùng HTTPS/TLS.                                                   | 4              | 0 nếu không mã hóa; 4 nếu tất cả giao tiếp đều được mã hóa.                                         |
| - Giới hạn tốc độ truy cập   | Sử dụng rate limiting hoặc throttling để chống DDoS.                                     | 4              | 0 nếu không có cơ chế; 4 nếu triển khai tự động.                                                    |
| - Kiểm tra đầu vào           | Xác thực và làm sạch dữ liệu đầu vào để chống tấn công (SQLi, XSS).                       | 4              | 0 nếu không kiểm tra; 4 nếu kiểm tra đầy đủ và định kỳ.                                             |
| **2. Bảo vệ dữ liệu**         |                                                                                          |                |                                                                                                     |
| - Mã hóa dữ liệu lưu trữ     | Sử dụng AES-256 hoặc tương đương cho dữ liệu nhạy cảm.                                   | 4              | 0 nếu không mã hóa; 4 nếu mọi dữ liệu quan trọng đều mã hóa.                                        |
| - Sao lưu và khôi phục       | Sao lưu tự động và kiểm tra khôi phục thường xuyên.                                      | 4              | 0 nếu không sao lưu; 4 nếu kiểm tra định kỳ và đảm bảo an toàn.                                     |
| **3. Quản lý cấu hình**       |                                                                                          |                |                                                                                                     |
| - Công cụ quản lý cấu hình   | Sử dụng Terraform, Ansible hoặc công cụ tự động khác.                                    | 4              | 0 nếu cấu hình thủ công; 4 nếu cấu hình được tự động hóa hoàn toàn.                                |
| - Kiểm tra cấu hình định kỳ  | Đánh giá cấu hình dựa trên tiêu chuẩn CIS.                                               | 4              | 0 nếu không kiểm tra; 4 nếu có lịch trình kiểm tra định kỳ.                                         |
| **4. An ninh mạng**           |                                                                                          |                |                                                                                                     |
| - Phân đoạn mạng             | Sử dụng chính sách phân đoạn mạng để cô lập microservices quan trọng.                   | 4              | 0 nếu không có phân đoạn; 4 nếu áp dụng phân đoạn toàn diện.                                       |
| - Sử dụng giao thức bảo mật  | Giao tiếp giữa microservices dùng mTLS hoặc tương đương.                                | 4              | 0 nếu không có giao thức bảo mật; 4 nếu mọi giao tiếp đều bảo mật.                                 |
| **5. Giám sát và nhật ký**    |                                                                                          |                |                                                                                                     |
| - Ghi nhật ký sự kiện an ninh| Ghi nhận đầy đủ và lưu trữ tập trung các sự kiện quan trọng.                             | 4              | 0 nếu không có hoặc thiếu sót; 4 nếu ghi nhật ký đầy đủ và theo dõi thường xuyên.                   |
| - Cảnh báo bất thường        | Tự động gửi cảnh báo khi phát hiện hành vi bất thường.                                  | 4              | 0 nếu không có cơ chế cảnh báo; 4 nếu tích hợp với công cụ như Prometheus hoặc ELK.                 |
| - Phân tích nhật ký          | Sử dụng công cụ phân tích để tìm kiếm các mối đe dọa.                                   | 4              | 0 nếu không phân tích; 4 nếu phân tích nhật ký thường xuyên và chi tiết.                           |
| - Kiểm tra bảo mật tự động   | Tích hợp kiểm tra bảo mật tự động trong quy trình CI/CD.                                | 4              | 0 nếu không kiểm tra; 4 nếu kiểm tra đầy đủ trong mọi lần triển khai.                              |
| - Quản lý lỗ hổng            | Sử dụng công cụ để phát hiện và quản lý các lỗ hổng trong hệ thống.                     | 4              | 0 nếu không có công cụ; 4 nếu có quy trình xử lý và giám sát liên tục.                             |
| - Bảo mật lưu trữ container  | Container được cấu hình để ngăn chặn ghi đè không được phép.                            | 4              | 0 nếu không có cơ chế; 4 nếu thực hiện đầy đủ.                                                     |
| - Quản lý bí mật             | Sử dụng Vault hoặc Secret Manager cho thông tin nhạy cảm.                               | 4              | 0 nếu không có công cụ; 4 nếu triển khai đầy đủ.                                                   |
| - Chính sách danh sách trắng IP | Giới hạn truy cập mạng chỉ từ IP được phê duyệt.                                       | 4              | 0 nếu không thực hiện; 4 nếu áp dụng toàn diện.                                                    |
| - Hệ thống phát hiện xâm nhập (IDS) | Triển khai IDS để giám sát hoạt động bất thường.                                   | 4              | 0 nếu không có; 4 nếu tích hợp với hệ thống báo cáo sự cố.                                         |
| - Đăng nhập không đặc quyền  | Không cho phép tài khoản root hoặc admin đăng nhập trực tiếp.                           | 4              | 0 nếu không có biện pháp; 4 nếu áp dụng đầy đủ.                                                    |
| - Cô lập dữ liệu             | Cô lập hoàn toàn dữ liệu ứng dụng khỏi hệ điều hành container.                          | 4              | 0 nếu không thực hiện; 4 nếu đảm bảo cô lập hoàn toàn.                                             |
| - Bảo vệ host                | Sử dụng công cụ như Falco để phát hiện hành vi đáng ngờ trong host.                     | 4              | 0 nếu không áp dụng; 4 nếu tích hợp và giám sát đầy đủ.                                            |
| - Chính sách quản lý ảnh container | Quét và xác minh chữ ký trước khi sử dụng ảnh container.                            | 4              | 0 nếu không quét; 4 nếu áp dụng đầy đủ.                                                            |
| - Phân đoạn VLAN             | Cách ly microservices trong các VLAN khác nhau.                                         | 4              | 0 nếu không cách ly; 4 nếu áp dụng đầy đủ.                                                         |

---

## 3. Phần B: Ứng Dụng Microservices (100 điểm)

| **Tiêu Chí**                 | **Mô Tả**                                                                                  | **Điểm Tối Đa** | **Hướng Dẫn Chấm**                                                                                   |
|-----------------------------|------------------------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------------|
| **1. Thiết kế dịch vụ**       |                                                                                          |                |                                                                                                     |
| - Tách biệt trách nhiệm      | Mỗi microservice đảm nhận một nhiệm vụ cụ thể (Single Responsibility Principle).          | 4              | 0 nếu nhiệm vụ chồng chéo; 4 nếu rõ ràng, độc lập.                                                  |
| - Tự phục hồi               | Microservices có khả năng tự phục hồi khi gặp lỗi.                                       | 4              | 0 nếu phụ thuộc hoàn toàn vào hệ thống bên ngoài; 4 nếu tự phục hồi được.                          |
| - Phân tách dữ liệu          | Mỗi dịch vụ có cơ sở dữ liệu riêng, không chia sẻ schema.                                | 4              | 0 nếu dùng chung; 4 nếu tách biệt hoàn toàn.                                                       |
| **2. Bảo mật ứng dụng**       |                                                                                          |                |                                                                                                     |
| - Mã hóa thông tin nhạy cảm | Mọi thông tin nhạy cảm đều được mã hóa trước khi xử lý.                                   | 4              | 0 nếu không mã hóa; 4 nếu mọi thông tin nhạy cảm đều được bảo mật.                                 |
| - Chính sách truy cập       | Áp dụng nguyên tắc tối thiểu quyền (Least Privilege).                                    | 4              | 0 nếu quyền không được quản lý; 4 nếu có chính sách kiểm soát rõ ràng.                             |
| - Bảo mật đầu vào            | Kiểm tra và làm sạch mọi dữ liệu đầu vào từ người dùng.                                  | 4              | 0 nếu không kiểm tra; 4 nếu kiểm tra đầy đủ và thường xuyên.                                       |
| **3. Đảm bảo chất lượng**     |                                                                                          |                |                                                                                                     |
| - Kiểm thử định kỳ          | Mọi microservices được kiểm thử định kỳ với các bộ công cụ tự động.                      | 4              | 0 nếu không kiểm thử; 4 nếu kiểm thử toàn diện và tự động hóa.                                      |
| - Giám sát hiệu suất        | Sử dụng APM (Application Performance Monitoring) để theo dõi hiệu suất.                   | 4              | 0 nếu không có công cụ APM; 4 nếu tích hợp công cụ giám sát hiệu suất.                             |
| - Đo lường độ trễ           | Theo dõi và tối ưu độ trễ giữa các dịch vụ.                                              | 4              | 0 nếu không đo lường; 4 nếu có hệ thống đo và cải thiện.                                           |
| - Kiểm tra tải              | Thực hiện kiểm tra tải để đảm bảo hiệu suất dưới áp lực.                                 | 4              | 0 nếu không kiểm tra; 4 nếu có kiểm tra định kỳ và cải tiến hiệu suất.                             |
| **4. Bảo mật bổ sung**              |                                                                                              |                |                                                                                                     |
| - Kiểm soát session                | Hết hiệu lực session tự động sau một thời gian không hoạt động.                              | 4              | 0 nếu không áp dụng; 4 nếu có cơ chế hết hiệu lực tự động.                                          |
| - Bảo vệ chống CSRF                | Sử dụng mã thông báo CSRF trong các yêu cầu trạng thái.                                      | 4              | 0 nếu không sử dụng mã thông báo CSRF; 4 nếu sử dụng hiệu quả.                                      | 
| - Cảnh báo thất bại đăng nhập      | Gửi cảnh báo khi có nhiều lần đăng nhập thất bại.                                            | 4              | 0 nếu không có cảnh báo; 4 nếu có hệ thống cảnh báo đầy đủ.                                          |
| - Tự động kiểm tra đầu cuối        | Tích hợp kiểm tra E2E cho các lỗ hổng bảo mật.                                               | 4              | 0 nếu không có kiểm tra; 4 nếu có kiểm tra bảo mật E2E tự động.                                     | 
| - Chính sách lưu trữ log           | Mã hóa log và chỉ giữ dữ liệu trong thời gian quy định.                                      | 4              | 0 nếu không mã hóa hoặc lưu trữ lâu dài; 4 nếu mã hóa và lưu trữ có hạn.                           |
| - Xử lý lỗi an toàn                | Không tiết lộ thông tin nhạy cảm qua thông báo lỗi.                                           | 4              | 0 nếu thông báo lỗi chứa thông tin nhạy cảm; 4 nếu bảo vệ thông tin nhạy cảm trong thông báo lỗi.  | 
| - Đánh giá bảo mật API            | Tích hợp công cụ API Gateway với bảo mật mở rộng.                                            | 4              | 0 nếu không tích hợp bảo mật; 4 nếu tích hợp đầy đủ API Gateway với bảo mật mở rộng.              | 
| - Kiểm tra thường xuyên với OWASP ZAP | Sử dụng OWASP ZAP để kiểm tra các endpoint.                                               | 4              | 0 nếu không sử dụng OWASP ZAP; 4 nếu kiểm tra đầy đủ các endpoint với OWASP ZAP.                   |
| - Theo dõi các sự kiện chuỗi cung ứng | Xác minh nguồn gốc thư viện và module bên thứ ba.                                          | 4              | 0 nếu không kiểm tra; 4 nếu có hệ thống xác minh nguồn gốc của tất cả thư viện và module.          | 
| - Phát hiện sự khác biệt trong hành vi API | Sử dụng AI để phát hiện hành vi không mong muốn.                                           | 4              | 0 nếu không sử dụng AI; 4 nếu có hệ thống AI để phát hiện hành vi không mong muốn.                | 
| - Tích hợp đa yếu tố xác thực (MFA) | Sử dụng MFA cho tất cả các endpoint quản trị.                                               | 4              | 0 nếu không áp dụng MFA; 4 nếu áp dụng MFA cho tất cả endpoint quản trị.                            | 
| - Phân tích tác động bảo mật của CI/CD | Kiểm tra pipeline CI/CD cho lỗ hổng.                                                        | 4              | 0 nếu không kiểm tra; 4 nếu có kiểm tra pipeline CI/CD định kỳ.                                     | 
| - Phân tích hành vi người dùng (UEBA) | Giám sát hành vi và phát hiện sự bất thường.                                               | 4              | 0 nếu không giám sát hành vi người dùng; 4 nếu giám sát và phát hiện bất thường hiệu quả.           | 
| - Đánh giá quyền truy cập đối với nhân viên | Xem xét quyền truy cập định kỳ.                                                           | 4              | 0 nếu không đánh giá; 4 nếu có đánh giá định kỳ và cập nhật quyền truy cập.                        | 
| - Kiểm thử bảo mật giả lập         | Tổ chức các bài kiểm thử giả lập tấn công (Red Team).                                       | 4              | 0 nếu không có kiểm thử; 4 nếu có kiểm thử giả lập tấn công định kỳ.                                | 


## **4. Tổng điểm và đánh giá**

| **Tổng Điểm** | **Xếp Loại An Toàn**          |
|---------------|-------------------------------|
| **90-100**    | An toàn cao (Đáp ứng tốt)     |
| **75-89**     | Tương đối an toàn (Đáp ứng)   |
| **50-74**     | Trung bình (Cần cải thiện)    |
| **<50**       | Nguy cơ cao (Cần khắc phục ngay) |

## **5. Tài liệu tham khảo**
- **NIST SP 800-204**: [Link](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204.pdf)  
- **CIS Docker Benchmark**: [Link](https://www.cisecurity.org/benchmark/docker)  
- **OWASP Microservices Security Cheat Sheet**: [Link](https://cheatsheetseries.owasp.org/cheatsheets/Microservices_Security_Cheat_Sheet.html)

# old version

# Hệ Thống Chấm Điểm An Toàn Thông Tin Cho Microservices (Claude Version)

_Cập nhật: 2025-01-14 14:08:47 UTC_
_Người tạo: frozenproof_

Hệ thống chấm điểm này dựa trên các tiêu chuẩn quốc tế như **ISO/IEC 27001**, **NIST SP 800-53**, và **OWASP Microservices Security**. Tổng điểm là **200**, chia thành hai phần chính: **Cơ sở hạ tầng Microservices (100 điểm)** và **Ứng dụng Microservices (100 điểm)**.

---

## 1. Hướng Dẫn Chấm Điểm Chung
- **0 điểm**: Không triển khai.
- **1 điểm**: Triển khai cơ bản nhưng không đầy đủ.
- **2 điểm**: Triển khai nhưng chưa kiểm tra thường xuyên.
- **3 điểm**: Triển khai đầy đủ, kiểm tra định kỳ.
- **4 điểm**: Triển khai tối ưu, cải tiến liên tục.

---

## 2. Phần A: Cơ Sở Hạ Tầng Microservices (100 điểm)

**1. Bảo mật API & Gateway (16 điểm)**
| Tiêu Chí | Mô Tả | Điểm Tối Đa | Hướng Dẫn Chấm | Tham Chiếu Tài Liệu |
|----------|--------|-------------|----------------|-------------------|
| - Xác thực API | Sử dụng OAuth 2.0 hoặc OpenID Connect. | 4 | 0 nếu không có xác thực; 4 nếu sử dụng tiêu chuẩn mạnh. | NIST SP 800-204 Sec 4.3.1; OWASP MS-4 |
| - Mã hóa truyền tải | Mọi giao tiếp API đều dùng HTTPS/TLS. | 4 | 0 nếu không mã hóa; 4 nếu tất cả giao tiếp đều được mã hóa. | NIST SP 800-204 Sec 4.4; OWASP MS-3 |
| - Giới hạn tốc độ truy cập | Sử dụng rate limiting hoặc throttling để chống DDoS. | 4 | 0 nếu không có cơ chế; 4 nếu triển khai tự động. | NIST SP 800-204 Sec 5.2.3; OWASP MS-8 |
| - Quản lý Certificate Lifecycle | Tự động quản lý vòng đời và gia hạn chứng chỉ SSL/TLS. | 4 | 0 nếu quản lý thủ công; 4 nếu tự động hoàn toàn với cảnh báo trước hạn. | NIST SP 800-204 Sec 4.4.3; OWASP MS-3 |
**2. Kiểm Soát Truy Cập & Bảo Mật Dữ Liệu (20 điểm)**
| - Mã hóa dữ liệu lưu trữ | Sử dụng AES-256 hoặc tương đương cho dữ liệu nhạy cảm. | 4 | 0 nếu không mã hóa; 4 nếu mọi dữ liệu quan trọng đều mã hóa. | NIST SP 800-204 Sec 4.5; CIS Docker 5.10 |
| - Kiểm soát truy cập phi tập trung | Triển khai ABAC/RBAC cho microservices. | 4 | 0 nếu không có; 4 nếu triển khai đầy đủ với chính sách chi tiết. | NIST SP 800-204 Sec 4.3.2; OWASP MS-4 |
| - Quản lý bí mật | Sử dụng Vault hoặc Secret Manager cho thông tin nhạy cảm. | 4 | 0 nếu không có công cụ; 4 nếu triển khai đầy đủ. | NIST SP 800-204 Sec 3.4; OWASP MS-3 |
| - Cô lập dữ liệu | Cô lập hoàn toàn dữ liệu ứng dụng khỏi hệ điều hành container. | 4 | 0 nếu không thực hiện; 4 nếu đảm bảo cô lập hoàn toàn. | CIS Docker 6.6; NIST SP 800-204 Sec 5.2.1 |
| - Sao lưu và khôi phục | Sao lưu tự động và kiểm tra khôi phục thường xuyên. | 4 | 0 nếu không sao lưu; 4 nếu kiểm tra định kỳ và đảm bảo an toàn. | NIST SP 800-204 Sec 6.3; CIS Docker 5.12 |
**3. Bảo Mật Network (20 điểm)**
| - Phân đoạn mạng | Sử dụng chính sách phân đoạn mạng để cô lập microservices. | 4 | 0 nếu không có phân đoạn; 4 nếu áp dụng phân đoạn toàn diện. | NIST SP 800-204 Sec 4.2; OWASP MS-2 |
| - Sử dụng giao thức bảo mật | Giao tiếp giữa microservices dùng mTLS. | 4 | 0 nếu không có giao thức bảo mật; 4 nếu mọi giao tiếp đều bảo mật. | NIST SP 800-204 Sec 4.4.2; OWASP MS-3 |
| - Phân đoạn VLAN | Cách ly microservices trong các VLAN khác nhau. | 4 | 0 nếu không cách ly; 4 nếu áp dụng đầy đủ. | NIST SP 800-204 Sec 3.9; OWASP MS-2 |
| - Chính sách danh sách trắng IP | Giới hạn truy cập mạng chỉ từ IP được phê duyệt. | 4 | 0 nếu không thực hiện; 4 nếu áp dụng toàn diện. | NIST SP 800-204 Sec 3.8; CIS Docker 3.7 |
| - Hệ thống phát hiện xâm nhập | Triển khai IDS để giám sát hoạt động bất thường. | 4 | 0 nếu không có; 4 nếu tích hợp với hệ thống báo cáo sự cố. | NIST SP 800-204 Sec 4.3; OWASP MS-7 |
**4. Bảo Mật Container (24 điểm)**
| - Bảo mật runtime container | Container được cấu hình với seccomp/AppArmor profiles. | 4 | 0 nếu không có cấu hình; 4 nếu áp dụng đầy đủ. | CIS Docker 5.25; NIST SP 800-204 Sec 5.2.5 |
| - Chính sách quản lý ảnh | Quét và xác minh chữ ký trước khi sử dụng ảnh. | 4 | 0 nếu không quét; 4 nếu áp dụng đầy đủ. | CIS Docker 6.3; NIST SP 800-204 Sec 5.2.2 |
| - Đăng nhập không đặc quyền | Không cho phép tài khoản root đăng nhập trực tiếp. | 4 | 0 nếu không có biện pháp; 4 nếu áp dụng đầy đủ. | NIST SP 800-204 Sec 3.3; CIS Docker 6.4 |
| - Cô lập tài nguyên | Giới hạn CPU, memory, storage cho mỗi container. | 4 | 0 nếu không giới hạn; 4 nếu có hard limits và monitoring. | CIS Docker 5.26; NIST SP 800-204 Sec 5.2.3 |
| - Bảo vệ host | Sử dụng Falco để phát hiện hành vi đáng ngờ. | 4 | 0 nếu không áp dụng; 4 nếu tích hợp và giám sát đầy đủ. | NIST SP 800-204 Sec 4.4; CIS Docker 2.13 |
| - Immutable Containers | Đảm bảo containers không thể bị thay đổi runtime. | 4 | 0 nếu containers có thể bị sửa đổi; 4 nếu hoàn toàn immutable. | CIS Docker 5.12; OWASP MS-5 |
**5. Giám Sát & Tuân Thủ (20 điểm)**
| - Ghi nhật ký sự kiện | Ghi nhận đầy đủ và lưu trữ tập trung sự kiện. | 4 | 0 nếu không có; 4 nếu ghi nhật ký đầy đủ. | NIST SP 800-204 Sec 6.2; CIS Docker 4.1 |
| - Cảnh báo bất thường | Tự động phát hiện và cảnh báo hành vi bất thường. | 4 | 0 nếu không có cơ chế; 4 nếu tích hợp với monitoring tools. | NIST SP 800-204 Sec 6.4; OWASP MS-7 |
| - Kiểm tra bảo mật tự động | Tích hợp security testing trong CI/CD. | 4 | 0 nếu không kiểm tra; 4 nếu kiểm tra đầy đủ mọi lần deploy. | NIST SP 800-204 Sec 5.3; OWASP MS-9 |
| - Quản lý lỗ hổng | Quét và quản lý CVEs trong toàn bộ hệ thống. | 4 | 0 nếu không có công cụ; 4 nếu có quy trình đầy đủ. | NIST SP 800-204 Sec 3.7; OWASP MS-6 |
| - Đồng bộ thời gian | Đồng bộ NTP cho toàn bộ hệ thống. | 4 | 0 nếu không đồng bộ; 4 nếu đồng bộ và giám sát liên tục. | CIS Docker 2.5; NIST SP 800-204 Sec 6.2.1 |

## 3. Phần B: Ứng Dụng Microservices (100 điểm)

| **Tiêu Chí** | **Mô Tả** | **Điểm Tối Đa** | **Hướng Dẫn Chấm** | **Tham Chiếu Tài Liệu** |
|--------------|-----------|-----------------|-------------------|------------------------|
| **1. Thiết kế dịch vụ** |||||
| - Tách biệt trách nhiệm | Mỗi microservice đảm nhận một nhiệm vụ cụ thể (Single Responsibility Principle). | 4 | 0 nếu nhiệm vụ chồng chéo; 4 nếu rõ ràng, độc lập. | NIST SP 800-204 Sec 3.1; OWASP MS-1 |
| - Tự phục hồi | Microservices có khả năng tự phục hồi khi gặp lỗi. | 4 | 0 nếu phụ thuộc hoàn toàn vào hệ thống bên ngoài; 4 nếu tự phục hồi được. | NIST SP 800-204 Sec 5.2.4; OWASP MS-7 |
| - Phân tách dữ liệu | Mỗi dịch vụ có cơ sở dữ liệu riêng, không chia sẻ schema. | 4 | 0 nếu dùng chung; 4 nếu tách biệt hoàn toàn. | NIST SP 800-204 Sec 4.5; OWASP MS-2 |
| **2. Bảo mật ứng dụng** |||||
| - Mã hóa thông tin nhạy cảm | Mọi thông tin nhạy cảm đều được mã hóa trước khi xử lý. | 4 | 0 nếu không mã hóa; 4 nếu mọi thông tin nhạy cảm đều được bảo mật. | NIST SP 800-204 Sec 4.5.1; OWASP MS-3 |
| - Chính sách truy cập | Áp dụng nguyên tắc tối thiểu quyền (Least Privilege). | 4 | 0 nếu quyền không được quản lý; 4 nếu có chính sách kiểm soát rõ ràng. | NIST SP 800-204 Sec 4.3.2; CIS Docker 5.1 |
| - Bảo mật đầu vào | Kiểm tra và làm sạch mọi dữ liệu đầu vào từ người dùng. | 4 | 0 nếu không kiểm tra; 4 nếu kiểm tra đầy đủ và thường xuyên. | OWASP MS-1; NIST SP 800-204 Sec 5.1 |
| **3. Bảo mật Container** |||||
| - Hardening Container Runtime | Cấu hình runtime với các chính sách bảo mật nghiêm ngặt (seccomp, AppArmor). | 4 | 0 nếu không có chính sách; 4 nếu áp dụng đầy đủ các profile bảo mật. | CIS Docker 5.25; NIST SP 800-204 Sec 5.2.5 |
| - Quét lỗ hổng ứng dụng | Quét CVE và các lỗ hổng bảo mật trong mã nguồn ứng dụng container. | 4 | 0 nếu không quét; 4 nếu tích hợp vào CI/CD với ngưỡng nghiêm ngặt. | NIST SP 800-204 Sec 5.3.1; OWASP MS-6 |
| - Cô lập tài nguyên | Giới hạn tài nguyên CPU, memory, và storage cho mỗi container. | 4 | 0 nếu không giới hạn; 4 nếu có cấu hình chi tiết và giám sát. | CIS Docker 5.26; NIST SP 800-204 Sec 5.2.3 |
| - Immutable Container | Đảm bảo container không thể bị thay đổi trong runtime. | 4 | 0 nếu container có thể bị sửa đổi; 4 nếu hoàn toàn immutable. | CIS Docker 5.12; OWASP MS-5 |
| **4. Quản lý Runtime Bảo mật** |||||
| - Kiểm soát Privileged Mode | Ngăn chặn container chạy ở chế độ privileged. | 4 | 0 nếu cho phép privileged; 4 nếu hoàn toàn unprivileged với exceptions được kiểm soát. | CIS Docker 5.4; NIST SP 800-204 Sec 5.2.6 |
| - Namespace Isolation | Cô lập hoàn toàn các namespace của container. | 4 | 0 nếu dùng chung namespace; 4 nếu cô lập triệt để. | CIS Docker 5.15; OWASP MS-5 |
| - Kernel Capability Control | Giới hạn chặt chẽ các kernel capability. | 4 | 0 nếu không giới hạn; 4 nếu áp dụng principle of least privilege. | CIS Docker 5.3; NIST SP 800-204 Sec 5.2.7 |

| **5. Bảo mật Image** |||||
| - Image Base Tối thiểu | Sử dụng minimal base image, loại bỏ các thành phần không cần thiết. | 4 | 0 nếu dùng full image; 4 nếu tối ưu hóa kích thước và thành phần. | CIS Docker 4.3; OWASP MS-5 |
| - Multistage Builds | Áp dụng multistage builds để giảm attack surface. | 4 | 0 nếu single stage; 4 nếu tối ưu hóa các layer. | CIS Docker 4.4; NIST SP 800-204 Sec 5.3.2 |
| - Image Signing | Thực thi chữ ký số cho container images. | 4 | 0 nếu không ký; 4 nếu có quy trình ký và xác thực nghiêm ngặt. | CIS Docker 4.5; OWASP MS-6 |

| **6. Bảo mật Mạng Container** |||||
| - Network Policy | Áp dụng chính sách mạng zero-trust giữa các container. | 4 | 0 nếu không có policy; 4 nếu có policies chi tiết. | NIST SP 800-204 Sec 4.2; OWASP MS-2 |
| - Service Mesh Security | Mã hóa và xác thực toàn bộ traffic trong service mesh. | 4 | 0 nếu không có bảo mật; 4 nếu áp dụng mTLS và policies. | NIST SP 800-204 Sec 4.4; OWASP MS-3 |
| - DNS Security | Bảo vệ và giám sát DNS queries của container. | 4 | 0 nếu không kiểm soát; 4 nếu có filtering và monitoring. | CIS Docker 3.18; NIST SP 800-204 Sec 4.2.3 |

| **7. Quản lý Secrets** |||||
| - Secret Rotation | Tự động rotation các secrets của container. | 4 | 0 nếu static secrets; 4 nếu có rotation tự động. | NIST SP 800-204 Sec 4.5.2; OWASP MS-3 |
| - Secret Access Control | Kiểm soát truy cập secrets theo nguyên tắc least privilege. | 4 | 0 nếu không kiểm soát; 4 nếu có RBAC chi tiết. | CIS Docker 5.6; NIST SP 800-204 Sec 4.3.2 |
| - Secret Storage Security | Mã hóa và bảo vệ storage chứa secrets. | 4 | 0 nếu không mã hóa; 4 nếu mã hóa end-to-end. | NIST SP 800-204 Sec 4.5; OWASP MS-3 |

| **8. Compliance và Audit** |||||
| - Container Audit Logging | Ghi log đầy đủ các hoạt động của container. | 4 | 0 nếu không có audit; 4 nếu log đầy đủ và được bảo vệ. | CIS Docker 2.12; NIST SP 800-204 Sec 6.2 |
| - Compliance Monitoring | Giám sát tuân thủ các tiêu chuẩn bảo mật container. | 4 | 0 nếu không giám sát; 4 nếu có báo cáo định kỳ. | NIST SP 800-204 Sec 6.4; OWASP MS-10 |
| - Security Baseline | Duy trì và kiểm tra baseline bảo mật cho mọi container. | 4 | 0 nếu không có baseline; 4 nếu có kiểm tra tự động. | CIS Docker 1.2; NIST SP 800-204 Sec 3.2 |

## **4. Tổng điểm và đánh giá**

| **Tổng Điểm** | **Xếp Loại An Toàn**          |
|---------------|-------------------------------|
| **90-100**    | An toàn cao (Đáp ứng tốt)     |
| **75-89**     | Tương đối an toàn (Đáp ứng)   |
| **50-74**     | Trung bình (Cần cải thiện)    |
| **<50**       | Nguy cơ cao (Cần khắc phục ngay) |

## **5. Tài liệu tham khảo**
- **NIST SP 800-204**: [Link](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204.pdf)  
- **CIS Docker Benchmark**: [Link](https://www.cisecurity.org/benchmark/docker)  
- **OWASP Microservices Security Cheat Sheet**: [Link](https://cheatsheetseries.owasp.org/cheatsheets/Microservices_Security_Cheat_Sheet.html)


