# 4.1. Nhập số lượng nhân viên
num_employees = int(input("Nhập số lượng nhân viên: "))

# 4.2. Nhập thông tin nhân viên
employees = []
for i in range(num_employees):
    name = input(f"Nhập tên nhân viên {i + 1}: ")
    days_worked = int(input(f"Nhập số ngày làm việc của {name}: "))
    employees.append((name, days_worked))

# 4.3. Kiểm tra dữ liệu hợp lệ
for name, days_worked in employees:
    if days_worked < 0 or days_worked > 22:
        print("Dữ liệu không hợp lệ")
        continue

    # 4.4. Kiểm tra nhân viên nghỉ toàn bộ
    if days_worked == 0:
        print(f"Nhân viên {name} nghỉ toàn bộ tháng")
        continue

    # 4.5. Hiển thị biểu đồ ngày làm việc
    print(f"Biểu đồ ngày làm việc của {name}:")
    for j in range(days_worked):
        print("*", end="")
    print()

    # 4.6. Thống kê mức độ làm việc
    for name, days_worked in employees:
        if days_worked >= 18:
            print(f"Nhân viên {name}: Làm việc chăm chỉ")
        elif days_worked < 10:
            print(f"Nhân viên {name}: Làm việc ít")
        else:
            print(f"Nhân viên {name}: Làm việc bình thường")