print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân: ")

# Áp dụng ép kiểu dữ liệu (Type Casting) từ str sang float
weight = float(input("Nhập cân nặng bệnh nhân: "))

print("--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân: ", name_patient)
print("Cân nặng đã nhập: ", weight)

# Trưởng nhóm IT viết thêm dòng này để kiểm tra dữ liệu của cân nặng
print("CẢNH BÁO - Kiểu dữ liệu đang lưu là: ", type(weight))




# 1. Phân Tích Lỗi (Bug Analysis)
# Dò luồng thực thi của chương trình (Trace code)
# Bước 1: Hệ thống yêu cầu nhập tên bệnh nhân qua hàm input() và lưu vào biến name_patient.
# Bước 2: Hệ thống yêu cầu nhập cân nặng qua câu lệnh weight = input("Nhập cân nặng bệnh nhân: ").
# Khi điều dưỡng nhập vào 65.5, giá trị này được gán trực tiếp cho biến weight.
# Bước 3: Hệ thống thực hiện in thông tin ra màn hình để kiểm tra.
# Bước 4: Hàm type(weight) được gọi để kiểm tra kiểu dữ liệu của biến weight.
#  Kết quả trả về và in ra màn hình là <class 'str'>.