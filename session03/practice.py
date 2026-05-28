# Lựa chọn duy trì chương trình của người dùng
choice = True

while choice:
    # 1. Nhập số lượng nhân viên cần quản lý
    employee_number = int(input("Nhập số lượng nhân viên: "))

    # 2. Vòng lặp nhập thông tin cho từng nhân viên (Dùng đúng tên biến employee_number)
    for employee_id in range(0, employee_number):
        print(f"\nNhân viên {employee_id + 1}")
        
        # Nhập tên và số ngày làm việc
        full_name = input("Tên: ")
        work_days = int(input("Số ngày đi làm: "))
        
        # 3. Hiển thị lại thông tin vừa nhập đúng theo form mẫu
        print("Thông tin nhân viên:")
        print(f"Tên: {full_name}")
        print(f"Số ngày đi làm: {work_days}")
        
        # 4. Đánh giá chuyên cần (Đặt NGAY TRONG vòng lặp for để áp dụng cho từng người)
        if work_days >= 20:
            print("Nhân viên chuyên cần tốt")
        else:
            print("Cần cải thiện chuyên cần")

    # 5. Hỏi tiếp tục hoặc kết thúc (Đặt NGOÀI vòng lặp for, bên trong vòng lặp while)
    print("") # In dòng trống cho thoáng giống mẫu
    confirm = input("Tiếp tục chương trình? (y/n): ")
    
    # Nếu người dùng nhập bất kỳ ký tự nào khác 'y' (ví dụ 'n'), vòng lặp while sẽ dừng
    if confirm == "y":
        choice = True
    else:
        choice = False
        print("Chương trình kết thúc")