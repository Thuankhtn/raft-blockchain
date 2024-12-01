# RAFT-LAB1
# RAFT P2P Network

Dự án này mô phỏng một mạng phân tán sử dụng thuật toán RAFT để đồng thuận trong một mạng peer-to-peer (P2P). Các nút trong mạng giao tiếp với nhau qua gRPC để thực hiện các cuộc bầu cử, đồng bộ hóa dữ liệu và xử lý các tình huống lỗi.

## Yêu Cầu Hệ Thống

- Python 3.x
- MongoDB (nếu dự án sử dụng cơ sở dữ liệu)
- Các thư viện Python cần cài đặt (liệt kê trong `requirements.txt`)

## Cài Đặt

1. **Clone dự án về máy**:

   ```bash
   git clone https://github.com/Thuankhtn/raft-blockchain.git
   cd project-name
2. **Tạo môi trường ảo và cài đặt các phụ thuộc**:
 
    bash: python -m venv venv
    bash: source venv/bin/activate  # Trên macOS/Linux
    bash: .\venv\Scripts\activate  # Trên Windows
    pip install -r requirements.txt
3. ** Cấu Hình mongoDB **:
    https://www.mongodb.com/try/download/community
4. **Run the following command to run the program**
```bash
cd D:\RAFT-LAB1
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. raft.proto # Generate the gRPC files
```