# Dựa trên kết quả debug ở yêu cầu 1, hãy tiến hành chỉnh sửa trực tiếp vào file mã nguồn để tối ưu hóa bài toán:
# Sửa lỗi Logic & Logging: Khắc phục triệt để lỗi tính phí vận chuyển khi khoảng cách từ 20km trở lên. Thay đổi cấu hình basicConfig để hệ thống hiển thị được đầy đủ các mức độ log từ INFO trở đi (để thấy được luồng chạy bình thường của hàm).
# Xử lý ngoại lệ chặt chẽ (Clean Code): Sửa lại đoạn kiểm tra distance <= 0. Yêu cầu hệ thống phải ném ra ngoại lệ raise ValueError("Distance must be positive") để chặn dữ liệu sai ngay từ đầu, thay vì chỉ log thông báo và trả về 0.0.
