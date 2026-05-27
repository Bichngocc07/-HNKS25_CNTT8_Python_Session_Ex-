print("--- TIẾP NHẬN VÀ CHUẨN HÓA SINH HIỆU ---")

patient_id_raw = input("Nhập mã bệnh nhân: ")
temperature_raw = input("Nhập nhiệt độ cơ thể: ")
heart_rate_raw = input("Nhập nhịp tim: ")


temperature_cleaned = temperature_raw.replace(",", ".")

patient_id = patient_id_raw.strip()
temperature = float(temperature_cleaned)
heart_rate = int(heart_rate_raw)

print("\n" + "="*15 + " KẾT QUẢ CHUẨN HÓA DỮ LIỆU " + "="*15)
print(f"Mã bệnh nhân: {patient_id}")
print(f"Nhiệt độ cơ thể: {temperature} độ C")
print(f" => Kiểu dữ liệu hệ thống ghi nhận: {type(temperature)}")
print(f"Nhịp tim: {heart_rate} nhịp/phút")
print(f" => Kiểu dữ liệu hệ thống ghi nhận: {type(heart_rate)}")
print("-" * 57)
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")
print("=" * 57)

# 1. Phân Tích và Đề Xuất Giải Pháp
# Phân tích Input / Output
# Dữ liệu đầu vào (Input): * Tất cả dữ liệu nhận từ hàm input() mặc định đều là kiểu chuỗi ký tự (str).
# Mã bệnh nhân: Chuỗi ký tự (Ví dụ: "BN999").
# Nhiệt độ cơ thể: Chuỗi ký tự số (Ví dụ: "37.5").
# Nhịp tim: Chuỗi ký tự số (Ví dụ: "85").
# Kiểu dữ liệu đầu ra mong muốn sau chuẩn hóa (Output):
# Mã bệnh nhân: Giữ nguyên kiểu chuỗi (str).
# Nhiệt độ cơ thể: Phải được chuyển thành số thực (float).
# Nhịp tim: Phải được chuyển thành số nguyên (int).
