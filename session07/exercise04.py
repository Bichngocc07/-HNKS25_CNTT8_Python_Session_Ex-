raw_data = "  emp-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    print("===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")
    print("====================================")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    print("") 
    
    if choice == "1":
        print("Chuỗi dữ liệu gốc hiện tại trên hệ thống:")
        print(f"'{raw_data}'\n")
        
    elif choice == "2":
        employee_list = raw_data.split("|")
        
        print("-" * 75)
        print(f"{'MÃ ID':<10} | {'HỌ VÀ TÊN':<20} | {'SỐ ĐIỆN THOẠI':<15} | {'PHÒNG BAN':<10}")
        print("-" * 75)
        
        for item in employee_list:
            info = item.split(";")
            
            emp_id = info[0].strip().upper()
            full_name = info[1].strip().title()
            department = info[3].strip().upper()
            
            raw_phone = info[2].strip()
            clean_phone = ""
            for char in raw_phone:
                if char != "-":
                    clean_phone += char
                    
            if clean_phone.isdigit() and len(clean_phone) == 10:
                formatted_phone = "******" + clean_phone[-4:]
            else:
                formatted_phone = "Invalid Format"
                
            print(f"{emp_id:<10} | {full_name:<20} | {formatted_phone:<15} | {department:<10}")
            
        print("-" * 75 + "\n")
        
    elif choice == "3":
        search_id = input("Nhập mã nhân viên cần tìm (Ví dụ: emp-002): ").strip().upper()
        
        is_found = False
        
        employee_list = raw_data.split("|")
        
        for item in employee_list:
            info = item.split(";")
            current_id = info[0].strip().upper()
            
            if current_id == search_id:
                is_found = True
                
                full_name = info[1].strip().title()
                department = info[3].strip().upper()
                
                raw_phone = info[2].strip()
                clean_phone = ""
                for char in raw_phone:
                    if char != "-":
                        clean_phone += char
                        
                if clean_phone.isdigit() and len(clean_phone) == 10:
                    formatted_phone = "******" + clean_phone[-4:]
                else:
                    formatted_phone = "Invalid Format"
                    
                print(f"\n[THÔNG TIN NHÂN VIÊN ĐƯỢC TÌM THẤY]:")
                print(f" - Mã nhân viên: {current_id}")
                print(f" - Họ và tên   : {full_name}")
                print(f" - Số điện thoại: {formatted_phone}")
                print(f" - Phòng ban   : {department}\n")
                break 
                
        if is_found == False:
            print("=> Không tìm thấy nhân viên\n")
            
    elif choice == "4":
        print("Thoát chương trình!")
        print("Hệ thống quản lý dữ liệu nhân sự đã đóng an toàn.")
        break 
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!\n")
