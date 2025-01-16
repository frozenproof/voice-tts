# TIÊU CHUẨN ĐÁNH GIÁ BẢO MẬT MICROSERVICES 
```
Version: 2025.1
Created: 2025-01-14 15:06:35 UTC
Updated: 2025-01-15 08:40:50 UTC
Author: frozenproof - QTuan
```
Hệ thống chấm điểm này dựa trên các tiêu chuẩn quốc tế như **ISO/IEC 27001**, **NIST SP 800-53**, và **OWASP Microservices Security**. Tổng điểm là **200**, chia thành hai phần chính: **Cơ sở hạ tầng Microservices (100 điểm)** và **Ứng dụng Microservices (100 điểm)**.

---

## 1. Hướng Dẫn Chấm Điểm Chung
- **0 điểm**: Không triển khai.
- **1 điểm**: Triển khai cơ bản nhưng không đầy đủ.
- **2 điểm**: Triển khai nhưng chưa kiểm tra thường xuyên.
- **3 điểm**: Triển khai đầy đủ, kiểm tra định kỳ.
- **4 điểm**: Triển khai tối ưu, cải tiến liên tục.

---

## Phần A: Cơ Sở Hạ Tầng Microservices (100 điểm)

**1. Quản Lý Truy Cập & Xác Thực (Access Control & Authentication) (20 điểm)**  
| **Tiêu Chí**             | **Mô Tả**                                            | **Điểm** | **Hướng Dẫn Chấm**                                 | **Tham Chiếu**                   |
|-|-|-|-|-|
| A1.1. Authentication Framework | Triển khai OAuth2/OIDC với xác thực và kiểm tra token | 4        | 0: basic auth; 1: JWT; 2: OAuth2 cơ bản; 3: OIDC; 4: custom claims | MSA Book p.134; NIST SP 800-204 4.3.1 |
| A1.2. Certificate Lifecycle | Tự động quản lý vòng đời của chứng chỉ SSL/TLS      | 4        | 0: thủ công; 2: tự động gia hạn; 4: tự động + giám sát | CIS K8s 1.2.21; CIS Docker 2.7 |
| A1.3. RBAC/ABAC           | Áp dụng kiểm soát truy cập dựa trên vai trò và thuộc tính | 4        | 0: không dùng RBAC; 2: RBAC cơ bản; 4: RBAC/ABAC đầy đủ | CIS K8s 5.1.1; NIST 800-204 4.3.2 |
| A1.4. Service Account     | Quản lý service accounts với principle of least privilege | 4        | 0: mặc định; 2: custom SA; 4: minimal privilege | CIS K8s 5.1.5; OWASP MS-4 |
| A1.5. Privileged Access   | Kiểm soát nghiêm ngặt đặc quyền root/admin           | 4        | 0: không hạn chế; 2: hạn chế một phần; 4: hạn chế hoàn toàn | CIS Docker 5.1; CIS K8s 4.2.6 |

**2. Bảo Mật Mạng (Network Security) (20 điểm)**  
| **Tiêu Chí**             | **Mô Tả**                                            | **Điểm** | **Hướng Dẫn Chấm**                                 | **Tham Chiếu**                   |
|-|-|-|-|-|
| A2.1. Network Policies    | Áp dụng chính sách Zero-trust cho cluster networks  | 4        | 0: mở; 2: cơ bản; 4: zero-trust                   | CIS K8s 5.3.2; NIST 800-204 4.2 |
| A2.2. Service Mesh Security | Zero-trust networking với mTLS enforcement          | 4        | 0: không mesh; 1: TLS cơ bản; 2: mTLS bật; 3: kiểm soát policy; 4: zero-trust hoàn chỉnh | MSA Book p.213; NIST SP 800-204 4.4 |
| A2.3. Network Segmentation | Micro-segmentation với VLAN/VPC isolation           | 4        | 0: phẳng; 2: một phần; 4: phân đoạn đầy đủ       | CIS K8s 5.3.4; OWASP MS-2 |
| A2.4. Load Balancer       | Bảo mật cho ingress/egress và load balancers        | 4        | 0: công khai; 2: cơ bản; 4: bảo mật chặt chẽ     | CIS K8s 5.3.3; NIST 800-204 4.2.2 |
| A2.5. Container Network   | Cải thiện bảo mật Container network interface (CNI) | 4        | 0: mặc định; 2: cơ bản; 4: bảo mật               | CIS Docker 3.7; CIS K8s 5.3.5 |

**3. Quản Lý Dữ Liệu & Bí Mật (Data & Secrets Management) (16 điểm)**  
| **Tiêu Chí**             | **Mô Tả**                                            | **Điểm** | **Hướng Dẫn Chấm**                                 | **Tham Chiếu**                   |
|-|-|-|-|-|
| A3.1. Secrets Management  | Vault tích hợp và mã hóa bí mật khi lưu trữ         | 4        | 0: văn bản thuần túy; 2: mã hóa; 4: quản lý bằng Vault | CIS K8s 2.7; NIST 800-204 3.4 |
| A3.2. Data Encryption     | Mã hóa data-at-rest và data-in-transit              | 4        | 0: không; 2: một phần; 4: mã hóa toàn bộ           | CIS K8s 1.2.31; NIST 800-204 4.5 |
| A3.3. ConfigMap Security  | Bảo vệ sensitive data trong ConfigMaps               | 4        | 0: công khai; 2: cơ bản; 4: mã hóa                | CIS K8s 5.4.1; OWASP MS-3 |
| A3.4. Storage Security    | Bảo mật PV/PVC và storage classes                   | 4        | 0: mặc định; 2: hạn chế; 4: bảo mật hoàn chỉnh   | CIS K8s 5.7.3; CIS Docker 5.3 |

**4. Bảo Mật Container & Pod (Container & Pod Security) (24 điểm)**  
| **Tiêu Chí**             | **Mô Tả**                                            | **Điểm** | **Hướng Dẫn Chấm**                                 | **Tham Chiếu**                   |
|-|-|-|-|-|
| A4.1. Container Image Security | Quét và ký image trong pipeline                     | 4        | 0: không quét; 1: quét cơ bản; 2: cơ sở dữ liệu lỗ hổng; 3: ký + quét; 4: kiểm soát admission | MSA Book p.256; CIS Docker 4.8 |
| A4.2. Pod Security Policies | Cấu hình PSP/Security Context                        | 4        | 0: không; 2: cơ bản; 4: PSP nghiêm ngặt           | CIS K8s 5.2.2; NIST 800-190 |
| A4.3. Resource Management  | Giới hạn tài nguyên container và quotas            | 4        | 0: không giới hạn; 2: giới hạn mềm; 4: giới hạn cứng | CIS K8s 5.2.4; CIS Docker 2.8 |
| A4.4. Runtime Security     | Bảo vệ runtime container (Seccomp, AppArmor)        | 4        | 0: tắt; 2: mặc định; 4: cấu hình tùy chỉnh       | CIS Docker 2.2; CIS K8s 5.2.7 |
| A4.5. Admission Control    | Kiểm soát policy với webhook và enforcement         | 4        | 0: không; 2: cơ bản; 4: chính sách nghiêm ngặt    | CIS K8s 1.2.7; NIST 800-204 4.8 |
| A4.6. Host Security       | Cải thiện bảo mật và isolation cho container host  | 4        | 0: mặc định; 2: cơ bản; 4: bảo mật hoàn chỉnh    | CIS Docker 2.1; CIS K8s 4.1.1 |

**5. Giám Sát & Tuân Thủ (Monitoring & Compliance) (20 điểm)**  
| **Tiêu Chí**             | **Mô Tả**                                            | **Điểm** | **Hướng Dẫn Chấm**                                 | **Tham Chiếu**                   |
|-|-|-|-|-|
| A5.1. Audit Logging       | Ghi nhật ký kiểm toán đầy đủ                        | 4        | 0: không có nhật ký; 2: cơ bản; 4: nhật ký kiểm toán có cấu trúc | CIS K8s 1.2.22; CIS Docker 2.12 |
| A5.2. Security Monitoring | Giám sát và phát hiện xâm nhập                      | 4        | 0: không; 2: IDS cơ bản; 4: IDS/IPS nâng cao      | CIS K8s 4.2.7; NIST 800-204 5.2 |
| A5.3. Compliance Scanning | Quét tuân thủ các benchmark CIS tự động            | 4        | 0: thủ công; 2: định kỳ; 4: tích hợp CI/CD        | CIS K8s 1.2.1; NIST 800-190 |
| A5.4. Incident Response   | Quy trình phản ứng sự cố tự động                    | 4        | 0: thủ công; 2: playbooks; 4: tự động sửa lỗi     | CIS K8s 1.2.8; NIST 800-204 5.3 |
| A5.5. Performance Monitoring | Giám sát hiệu suất và sức khỏe của cluster         | 4        | 0: không; 2: chỉ số cơ bản; 4: quan sát đầy đủ    | CIS K8s 4.2.9; NIST 800-204 5.1 |

A5.3 Chưa thực sự rõ ràng.

## Tổng Kết Điểm Phần A:
1. Access Control & Authentication: 20 điểm
2. Network Security: 20 điểm
3. Data & Secrets Management: 16 điểm
4. Container & Pod Security: 24 điểm
5. Monitoring & Compliance: 20 điểm

Tổng cộng: 100 điểm

---
Notes:
1. Mỗi tiêu chí được đánh giá theo thang điểm từ 0-4
2. Tham chiếu bao gồm CIS Benchmarks cho cả Kubernetes và Docker
3. Hướng dẫn chấm điểm được thiết kế để dễ đánh giá khách quan
4. Các tiêu chuẩn được cập nhật theo CIS Kubernetes v1.23 trở lên

## 3. Phần B: Ứng Dụng Microservices (100 điểm)

**1. Thiết Kế và Kiến Trúc Microservices (20 điểm)**
| **Tiêu Chí** | **Mô Tả** | **Điểm** | **Hướng Dẫn Chấm** | **Tham Chiếu** |
|--------------|-----------|----------|-------------------|----------------|
| B1.1. Service Domain Isolation | Bounded context và domain isolation | 4 | 0: monolithic; 1: basic splits; 2: domain boundaries; 3: event-driven; 4: full DDD | MSA Book p.45; NIST SP 800-204 3.1 |
| B1.2. Resilience Design | Thiết kế khả năng phục hồi với circuit breakers và fallbacks | 4 | 0: không có resilience; 2: basic retries; 4: full resilience patterns | NIST SP 800-204 5.2.4; CIS K8s 5.2.8 |
| B1.3. Data Pattern Implementation | CQRS và event sourcing patterns | 4 | 0: shared DB; 1: separate DB; 2: CQRS basic; 3: event sourcing; 4: full patterns + monitoring | MSA Book p.167; NIST SP 800-204 4.5 |
| B1.4. API Design | RESTful/gRPC với versioning và contract testing | 4 | 0: no standards; 2: basic REST; 4: full API governance | NIST SP 800-204 4.1; CIS K8s 1.2.21 |
| B1.5. Service Mesh Integration | Istio/Linkerd với mTLS và traffic policies | 4 | 0: no mesh; 2: basic mesh; 4: full mesh capabilities | NIST SP 800-204 4.4; CIS K8s 5.3.2 |

**2. Bảo Mật Ứng Dụng và API (20 điểm)**
| **Tiêu Chí** | **Mô Tả** | **Điểm** | **Hướng Dẫn Chấm** | **Tham Chiếu** |
|--------------|-----------|----------|-------------------|----------------|
| B2.1. API Security | OAuth2/OIDC với rate limiting và threat protection | 4 | 0: no auth; 2: basic auth; 4: full OAuth2 + security | NIST SP 800-204 4.3; CIS K8s 1.2.7 |
| B2.2. Schema Validation | Schema validation và sanitization cho API endpoints | 4 | 0: không schema; 1: basic types; 2: OpenAPI/Swagger; 3: custom rules; 4: full pipeline + sanitization | OWASP API Sec 2023; OpenAPI 3.0 |
| B2.3. Output Encoding | Encoding đầu ra để ngăn chặn XSS và injection | 4 | 0: no encoding; 2: basic encoding; 4: context-aware encoding | OWASP MS-1; CIS K8s 5.2.5 |
| B2.4. Session Management | JWT với proper signing và rotation | 4 | 0: no session mgmt; 2: basic JWT; 4: full session security | NIST SP 800-204 4.3.3; CIS K8s 1.2.8 |
| B2.5. Error Handling | Xử lý lỗi an toàn không để lộ thông tin nhạy cảm | 4 | 0: exposed errors; 2: basic handling; 4: secure error handling | OWASP API Sec 7.0; CIS K8s 1.2.9 |

**3. Service Communication & Resilience (20 điểm)**
| **Tiêu Chí** | **Mô Tả** | **Điểm** | **Hướng Dẫn Chấm** | **Tham Chiếu** |
|--------------|-----------|----------|-------------------|----------------|
| B3.1. Circuit Breaker Pattern | Failure detection và graceful degradation | 4 | 0: no protection; 1: timeouts only; 2: basic breaker; 3: fallback config; 4: adaptive thresholds | MSA Book p.198; NIST SP 800-204 5.2.4 |
| B3.2. Health Check System | Health check probes và service discovery | 4 | 0: không check; 1: basic ping; 2: liveness/readiness; 3: custom metrics; 4: auto failover | NIST SP 800-204 4.2; K8s Probes |
| B3.3. Message Security | Bảo mật message queues và event streams | 4 | 0: plain text; 2: encryption; 4: full message security | NIST SP 800-204 4.4; OWASP MS-3 |
| B3.4. Retry Policies | Intelligent retries và backoff strategies | 4 | 0: no retries; 2: basic retry; 4: advanced retry policies | NIST SP 800-204 5.2.4; OWASP MS-7 |
| B3.5. Bulkhead Pattern | Service isolation và resource partitioning | 4 | 0: no isolation; 2: basic isolation; 4: complete bulkheads | NIST SP 800-204 5.2.3; OWASP MS-5 |

**4. Data Management & Privacy (20 điểm)**
| **Tiêu Chí** | **Mô Tả** | **Điểm** | **Hướng Dẫn Chấm** | **Tham Chiếu** |
|--------------|-----------|----------|-------------------|----------------|
| B4.1. Data Classification | Phân loại và kiểm soát dữ liệu theo mức độ nhạy cảm | 4 | 0: không phân loại; 1: basic labels; 2: data policies; 3: encryption rules; 4: full data governance | NIST SP 800-53 AC-1; ISO 27001 A.8.2 |
| B4.2. Event Sourcing | Bảo mật event store và event streams | 4 | 0: no events; 2: basic events; 4: secure event sourcing | NIST SP 800-204 4.5.2; OWASP MS-2 |
| B4.3. CQRS Security | Bảo mật read/write models riêng biệt | 4 | 0: shared model; 2: basic CQRS; 4: secure CQRS | NIST SP 800-204 4.5.1; OWASP MS-2 |
| B4.4. Data Consistency | Xử lý eventually consistent security | 4 | 0: no handling; 2: basic; 4: full consistency controls | NIST SP 800-204 4.5; OWASP MS-3 |
| B4.5. Data Lifecycle | Quản lý vòng đời dữ liệu cross-service | 4 | 0: no mgmt; 2: basic lifecycle; 4: full lifecycle security | NIST SP 800-204 4.5.3; OWASP MS-3 |

**5. Service Observability & Monitoring (20 điểm)**
| **Tiêu Chí** | **Mô Tả** | **Điểm** | **Hướng Dẫn Chấm** | **Tham Chiếu** |
|--------------|-----------|----------|-------------------|----------------|
| B5.1. Distributed Tracing | Tracing xuyên suốt các service calls | 4 | 0: no tracing; 2: basic traces; 4: full distributed tracing | NIST SP 800-204 6.2; OWASP MS-8 |
| B5.2. Security Metrics | Thu thập và phân tích metrics bảo mật | 4 | 0: không metrics; 1: basic logs; 2: SIEM integration; 3: alerts setup; 4: automated response | NIST SP 800-137; CIS Controls v8 |
| B8.3. Progressive Deployment | Triển khai theo stages với rollback capability | 4 | 0: full deploy; 1: manual stages; 2: 10% canary; 3: auto scale; 4: ML-based rollout | NIST SP 800-204 5.3; K8s Deployments |
| B5.4. Health Monitoring | Giám sát sức khỏe end-to-end services | 4 | 0: no health checks; 2: basic health; 4: advanced monitoring | NIST SP 800-204 6.3; OWASP MS-7 |
| B5.5. Anomaly Detection | Phát hiện bất thường trong service behavior | 4 | 0: no detection; 2: basic alerts; 4: ML-based detection | NIST SP 800-204 6.4; OWASP MS-10 |

**6. Service Authentication & Authorization (20 điểm)**
| **Tiêu Chí** | **Mô Tả** | **Điểm** | **Hướng Dẫn Chấm** | **Tham Chiếu** |
|--------------|-----------|----------|-------------------|----------------|
| B6.1. Service Identity | Quản lý định danh của từng microservice | 4 | 0: shared identity; 2: basic identity; 4: strong service identity | NIST SP 800-204 4.3.1; OWASP MS-4 |
| B6.2. Token Propagation | Truyền và xác thực token giữa services | 4 | 0: no propagation; 2: basic tokens; 4: secure token chain | NIST SP 800-204 4.3.2; OWASP MS-4 |
| B6.3. Fine-grained Auth | Kiểm soát quyền chi tiết cho từng API | 4 | 0: coarse auth; 2: role-based; 4: attribute-based access | NIST SP 800-204 4.3.3; OWASP MS-4 |
| B6.4. Delegation Flows | OAuth2/OIDC flows giữa services | 4 | 0: no delegation; 2: basic OAuth; 4: complete delegation | NIST SP 800-204 4.3.4; OWASP MS-4 |
| B6.5. Credential Security | Bảo vệ credentials trong distributed system | 4 | 0: exposed creds; 2: basic protection; 4: vault integration | NIST SP 800-204 4.3.5; OWASP MS-3 |

**7. Configuration & Secrets Management (20 điểm)**
| **Tiêu Chí** | **Mô Tả** | **Điểm** | **Hướng Dẫn Chấm** | **Tham Chiếu** |
|--------------|-----------|----------|-------------------|----------------|
| B7.1. Config Version Control | Quản lý version cho configs và audit trail | 4 | 0: static files; 1: git storage; 2: versioned; 3: review process; 4: automated validation | MSA Book p.187; NIST SP 800-204 4.5.2 |
| B7.2. Secret Lifecycle Management | Vault integration và secret rotation | 4 | 0: plaintext; 1: encrypted storage; 2: vault basic; 3: auto-rotation; 4: zero-trust secrets | MSA Book p.156; NIST SP 800-204 4.5.1 |
| B7.3. Environment Security | RBAC cho môi trường và config encryption | 4 | 0: shared access; 1: env separation; 2: RBAC basic; 3: encrypted configs; 4: full isolation | MSA Book p.192; OWASP MS-3 |
| B7.4. Dynamic Configuration | Service discovery và config updates | 4 | 0: static; 1: manual updates; 2: auto-reload; 3: validated changes; 4: atomic updates | MSA Book p.201; NIST SP 800-204 4.5.4 |
| B7.5. Secrets Distribution | Transport encryption và access control | 4 | 0: plain transport; 1: TLS basic; 2: mTLS; 3: token-based; 4: JIT access | MSA Book p.167; NIST SP 800-204 4.5.5 |

**8. Deployment & Testing Security (20 điểm)**
| **Tiêu Chí** | **Mô Tả** | **Điểm** | **Hướng Dẫn Chấm** | **Tham Chiếu** |
|--------------|-----------|----------|-------------------|----------------|
| B8.1. Security Pipeline | SAST, DAST và dependency scanning | 4 | 0: no scan; 1: SAST only; 2: SAST+DAST; 3: dependency scan; 4: full pipeline | MSA Book p.278; NIST SP 800-204 5.3.1 |
| B8.2. Deployment Gates | Security checkpoints trong CI/CD | 4 | 0: no gates; 1: basic checks; 2: vuln scan; 3: compliance check; 4: risk-based deploy | MSA Book p.289; NIST SP 800-204 5.3.2 |
| B8.3. Progressive Delivery | Blue-green và canary deployments | 4 | 0: direct deploy; 1: basic stages; 2: blue-green; 3: canary; 4: automated rollout | MSA Book p.295; NIST SP 800-204 5.3.3 |
| B8.4. Feature Security | Feature flags và A/B testing controls | 4 | 0: no controls; 1: basic flags; 2: secure flags; 3: monitored tests; 4: automated safety | MSA Book p.304; NIST SP 800-204 5.3.4 |
| B8.5. Incident Recovery | Automated rollback và state recovery | 4 | 0: manual recover; 1: basic rollback; 2: state backup; 3: auto rollback; 4: zero-downtime recovery | MSA Book p.312; NIST SP 800-204 5.3.5 |

## Tổng Kết và Đánh Giá

### Tổng Điểm Chi Tiết (160 điểm tối đa):
1. Thiết Kế và Kiến Trúc Microservices: 20 điểm (5 tiêu chí × 4 điểm)
2. Bảo Mật Ứng Dụng và API: 20 điểm (5 tiêu chí × 4 điểm)
3. Service Communication & Resilience: 20 điểm (5 tiêu chí × 4 điểm)
4. Data Management & Privacy: 20 điểm (5 tiêu chí × 4 điểm)
5. Service Observability & Monitoring: 20 điểm (5 tiêu chí × 4 điểm)
6. Service Authentication & Authorization: 20 điểm (5 tiêu chí × 4 điểm)
7. Configuration & Secrets Management: 20 điểm (5 tiêu chí × 4 điểm)
8. Deployment & Testing Security: 20 điểm (5 tiêu chí × 4 điểm)

### Hướng Dẫn Tính Điểm:
1. Tổng điểm tối đa: 160 điểm (40 tiêu chí × 4 điểm)
2. Công thức quy đổi: Điểm cuối = (Tổng điểm đạt được ÷ 160) × 100

### Bảng Xếp Loại An Toàn:
| **Điểm Quy Đổi** | **Xếp Loại** | **Đánh Giá và Khuyến Nghị** |
|------------------|---------------|----------------------------|
| 90-100 | Xuất Sắc | Đáp ứng đầy đủ yêu cầu bảo mật. Duy trì và cập nhật định kỳ |
| 80-89 | Tốt | Đáp ứng hầu hết yêu cầu. Cải thiện các điểm yếu còn lại |
| 70-79 | Đạt | Đáp ứng cơ bản. Lập kế hoạch nâng cấp trong 6 tháng |
| <70 | Cần Cải Thiện | Tồn tại nhiều rủi ro. Cần có kế hoạch khắc phục ngay |


### Tài Liệu Tham Khảo:
1. **NIST Special Publication 800-204**: Security Strategies for Microservices-based Application Systems
   - [https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204.pdf)
   - Referenced in sections: B1-B8 for security controls and architecture guidance

2. **OWASP Microservices Security**: Top 10 Microservices Security Best Practices
   - [https://cheatsheetseries.owasp.org/cheatsheets/Microservices_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Microservices_Security_Cheat_Sheet.html)
   - Referenced in sections: B2-B8 for security implementation guidelines

3. **CIS Benchmarks**: Security Configuration Guidance
   - CIS Docker Benchmark: [https://www.cisecurity.org/benchmark/docker](https://www.cisecurity.org/benchmark/docker)
   - CIS Kubernetes Benchmark: [https://www.cisecurity.org/benchmark/kubernetes](https://www.cisecurity.org/benchmark/kubernetes)
   - Referenced in sections: B3, B4 for container and orchestration security

### Tài Liệu Tham Khảo Bổ Sung:
4. **Microservices Security in Action** (Manning Publications, 2020)
   - Used as reference architecture and security patterns inspiration

### Giải Thích Các Viết Tắt (Shorthand) Trong Tài Liệu

Dưới đây là bảng giải thích toàn bộ các viết tắt (shorthand) từ hai tài liệu được cung cấp:

| **Viết Tắt**       | **Giải Thích**                                                                                           |
|---------------------|---------------------------------------------------------------------------------------------------------|
| **DDD**            | *Domain-Driven Design* – Thiết kế hướng miền, phương pháp tổ chức hệ thống tập trung vào các miền nghiệp vụ. |
| **mTLS**           | *Mutual Transport Layer Security* – Bảo mật tầng truyền với xác thực hai chiều giữa các dịch vụ.          |
| **DB**             | *Database* – Cơ sở dữ liệu.                                                                              |
| **RESTful**        | *Representational State Transfer* – Kiến trúc API tuân theo các quy tắc REST.                            |
| **gRPC**           | *gRPC Remote Procedure Call* – Giao thức gọi hàm từ xa hiệu quả, do Google phát triển.                   |
| **API**            | *Application Programming Interface* – Giao diện lập trình ứng dụng, cho phép các hệ thống giao tiếp.    |
| **OAuth2/OIDC**    | *OAuth 2.0 / OpenID Connect* – Giao thức xác thực và ủy quyền an toàn.                                   |
| **XSS**            | *Cross-Site Scripting* – Lỗ hổng bảo mật khi tập lệnh độc hại được thực thi trên trang web.              |
| **JWT**            | *JSON Web Token* – Chuẩn mở dùng để truyền thông tin dưới dạng JSON giữa các bên một cách an toàn.       |
| **E2E**            | *End-to-End* – Từ đầu đến cuối, thường dùng để chỉ quá trình kiểm tra hoặc giám sát toàn bộ hệ thống.    |
| **CI/CD**          | *Continuous Integration / Continuous Deployment* – Tích hợp liên tục và triển khai liên tục.             |
| **CQRS**           | *Command Query Responsibility Segregation* – Mô hình tách biệt giữa ghi lệnh (Command) và truy vấn (Query). |
| **ML**             | *Machine Learning* – Học máy, công nghệ sử dụng thuật toán để máy tính học từ dữ liệu.                   |
| **Istio/Linkerd**  | Công cụ *Service Mesh* – Quản lý và bảo mật giao tiếp giữa các dịch vụ microservices.                    |
| **Canary Deployment** | Phương pháp triển khai an toàn với thử nghiệm trên một phần nhỏ trước khi triển khai toàn diện.         |
| **OWASP**          | *Open Web Application Security Project* – Tổ chức phi lợi nhuận tập trung vào bảo mật ứng dụng web.      |
| **NIST SP**        | *National Institute of Standards and Technology Special Publication* – Các tài liệu hướng dẫn bảo mật của NIST. |
| **CIS K8s**        | *Center for Internet Security Kubernetes* – Hướng dẫn bảo mật dành cho Kubernetes.                      |
| **MS**             | *Microservices* – Các dịch vụ nhỏ độc lập, hợp tác với nhau để xây dựng ứng dụng.                        |
| **Vault**          | Giải pháp quản lý bảo mật và thông tin nhạy cảm (ví dụ như sản phẩm của HashiCorp.    )  |

