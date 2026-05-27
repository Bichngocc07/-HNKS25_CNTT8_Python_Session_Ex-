print("--- HỆ THỐNG PHÂN LUỒNG CẤP CỨU ---")
heart_rate = int(input("Nhập nhịp tim của bệnh nhân (nhịp/phút): "))

# Hệ thống phân loại mức độ ưu tiên chính xác theo quy tắc y khoa
if heart_rate > 120:
    # Đưa điều kiện nghiêm trọng nhất (Đỏ) lên đầu tiên
    print("Mức độ ưu tiên: ĐỎ - Tình trạng nguy kịch! Yêu cầu cấp cứu ngay lập tức.")
elif heart_rate > 100:
    # Điều kiện Vàng đứng thứ hai
    print("Mức độ ưu tiên: VÀNG - Bất thường. Cần theo dõi sát sao.")
elif heart_rate < 60:
    # Điều kiện Xanh dương dành cho nhịp tim chậm
    print("Mức độ ưu tiên: XANH DƯƠNG - Nhịp tim chậm. Yêu cầu siêu âm.")
else:
    # Các trường hợp còn lại (Từ 60 đến 100) rơi vào Xanh lá
    print("Mức độ ưu tiên: XANH LÁ - Ổn định. Vui lòng đợi ở sảnh chờ.")

print("Quá trình phân luồng hoàn thành.")


# 1. Phân Tích Lỗi (Bug Analysis)
# Dò luồng thực thi (Trace code) với test case heart_rate = 135Bước 1 (Nhập liệu): Biến heart_rate nhận giá trị số nguyên là 135.

# Bước 2 (Kiểm tra điều kiện đầu tiên): Hệ thống so sánh điều kiện tại câu lệnh if heart_rate > 100:.Vì $135 > 100$ là Đúng (True), chương trình 
# lập tức nhảy vào thực thi khối lệnh bên trong if.

# Bước 3 (In kết quả sai): Màn hình in ra dòng chữ: Priority: YELLOW – Abnormal. Monitor closely. (Mức độ Vàng).

# Bước 4 (Kết thúc nhánh rẽ): Do cấu trúc if-elif-else chỉ chọn duy nhất một nhánh khớp đầu tiên, toàn bộ các
#  điều kiện phía sau (bao gồm cả mức Đỏ > 120) bị bỏ qua hoàn toàn.

# Bước 5: In ra Triage process completed.