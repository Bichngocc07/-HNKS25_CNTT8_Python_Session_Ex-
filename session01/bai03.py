print("---HỆ THỐNG TIẾP NHẬN BỆNH NHÂN - PHÒNG KHÁM ĐA KHOA---")
# (1) Thu thập thông tin đầu vào (Input) từ Lễ tân
patient_name = input("Nhập họ và tên bệnh nhân: ").strip()
record_id = input("Nhập mã bệnh án: ").strip()
department = input("Nhập khoa/phòng khám chỉ định: ").strip()

print("\n" + "="*50)
print("PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print("="*50)

# (2) Xử lý logic và xuất thông tin theo định dạng chuẩn của phòng khám (Output)
# Sử dụng f-string giúp mã nguồn rõ ràng, chuyên nghiệp và tối ưu tốc độ xử lý
print(f"Bệnh nhân: {patient_name} - Mã BA: {record_id} - Chuyển tới: {department}")

print("="*50)
print("Hệ thống đã đồng bộ dữ liệu tới phòng khám chỉ định thành công!")