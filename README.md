# DatalakeStorage
_______________________
- MinIO Distributed Mode chạy 3 replicas trong Kubernetes Namespace minio:
<img width="1110" height="191" alt="Screenshot 2025-11-25 235018" src="https://github.com/user-attachments/assets/98a16dbd-a97b-421a-8410-dfe8ce569593" />

- Service MinIO kiểu Headless (clusterIP: None) phục vụ cho StatefulSet distributed
<img width="1402" height="115" alt="Screenshot 2025-11-25 235048" src="https://github.com/user-attachments/assets/ddcfed65-f522-448c-9e98-b20ef3185c63" />

- Port-forward MinIO API
<img width="1370" height="196" alt="Screenshot 2025-11-25 235534" src="https://github.com/user-attachments/assets/6cd3c2df-508b-4048-81ce-4c5644f219bb" />

- Port-forward MinIO Console
<img width="1383" height="191" alt="image" src="https://github.com/user-attachments/assets/d7c6a64d-47ee-433f-a27a-2de6e62f3dba" />

- Bucket datalake dùng để lưu trữ dữ liệu CSV trong Data Lake và sales.csv đã được upload vào MinIO (Object Storage)
<img width="2857" height="1616" alt="Screenshot 2025-11-25 235129" src="https://github.com/user-attachments/assets/6bda96d1-6c10-4daf-b00b-d803bbd73b07" />

- Tạo Presigned URL cho file sales.csv bằng MinIO Client (mc)
<img width="1387" height="489" alt="Screenshot 2025-11-25 235218" src="https://github.com/user-attachments/assets/4085539c-a09d-4683-919c-c9177233be4b" />

- Mã nguồn dùng DuckDB đọc dữ liệu CSV từ presigned URL
<img width="1396" height="298" alt="Screenshot 2025-11-25 235246" src="https://github.com/user-attachments/assets/4ea76cd4-943b-4acf-bff3-2e81be8dc222" />

