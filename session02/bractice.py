#Nhập thông tin bệnh nhân
user_name = input("Nhập tên bệnh nhân: ")
birth_year = int(input("Nhập năm sinh của bệnh nhân: "))
total_date = input(input("Nhập tổng số ngày bị bệnh: "))
body_temperature = float(input("Nhập nhiệt độ cơ thể của bệnh nhân: "))
cost = float(input("Nhập chi phí điều trị của bệnh nhân: "))

#Kiểm tra dữ liệu đầu vào
#Tên không được để trống
#Năm sinh phải nằm trong khoảng hợp lệ (1900 → năm hiện tại)
#Số ngày bị bệnh ≥ 0
#Nhiệt độ nằm trong khoảng 30 → 45°C
#Chi phí khám > 0
if user_name == "":
    print("Tên bệnh nhân không được để trống")
if birth_year < 1900 or birth_year > 2026:
    print("Năm sinh không hợp lệ")
if total_date < 0:
    print("Số ngày bị bệnh không hợp lệ")
if body_temperature < 30 or body_temperature > 45:
    print("Nhiệt độ cơ thể không hợp lệ")
if cost < 0:
    print("Chi phí điều trị không hợp lệ")


#Tính toán thông tin
my_age = 2026 - birth_year
surcharge = cost * 0.1 #tính phụ phí
total_cost = cost + surcharge #tính tổng chi phí

#Phân loại tinh trạng sức khỏe
# Nếu nhiệt độ > 38°C và số ngày bệnh > 3 → "Nguy hiểm"
# Nếu nhiệt độ > 38°C → "Sốt cao"
# Nếu nhiệt độ > 37.5°C → "Sốt nhẹ"
# Ngược lại → "Bình thường"
if body_temperature > 38 and total_date > 3:
    if my_age > 60:
        print("Cấp cứu")
    else:
        print("Ưu tiên cao")
else:
        print("Bình thường")

#Đánh giá mức chi phí
#Nếu tổng chi phí >50000000 → "Cao"
#Ngược lại → "Thấp"
evaluation = "Cao" if total_cost > 50000000 else "Thấp"
print(f"Đánh giá chi phí: {evaluation}")
#Đánh giá mức độ ưu tiên
#Đánh giá tri phí