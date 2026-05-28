choice = True

while choice:
    employee_number = int(input("Nhập số lượng nhân viên: "))

    for employee_id in range(0, employee_number):
        print(f"\nNhân viên {employee_id + 1}")
        
        full_name = input("Tên: ")
        work_days = int(input("Số ngày đi làm: "))
        
        print("Thông tin nhân viên:")
        print(f"Tên: {full_name}")
        print(f"Số ngày đi làm: {work_days}")
        
        if work_days >= 20:
            print("Nhân viên chuyên cần tốt")
        else:
            print("Cần cải thiện chuyên cần")

    print("") 
    confirm = input("Tiếp tục chương trình? (y/n): ")
    
    if confirm == "y":
        choice = True
    else:
        choice = False
        print("Chương trình kết thúc")
