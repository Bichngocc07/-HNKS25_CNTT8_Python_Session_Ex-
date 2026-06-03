# Chuỗi dữ liệu thô ban đầu của hệ thống CRM cũ
raw_data = "  emp-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

# Vòng lặp duy trì menu điều hướng liên tục
while True:
    print("===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")
    print("====================================")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    print("") # Xuống dòng cho thoáng
    
    # --- CHỨC NĂNG 1: Hiển thị chuỗi dữ liệu gốc ---
    if choice == "1":
        print("Chuỗi dữ liệu gốc hiện tại trên hệ thống:")
        print(f"'{raw_data}'\n")
        
    # --- CHỨC NĂNG 2: Chuẩn hóa dữ liệu và in báo cáo ---
    elif choice == "2":
        # Bước 1: Tách chuỗi thô thành danh sách từng nhân viên độc lập
        employee_list = raw_data.split("|")
        
        # Tiêu đề bảng báo cáo (Căn lề bằng f-string bám sát yêu cầu)
        print("-" * 75)
        print(f"{'MÃ ID':<10} | {'HỌ VÀ TÊN':<20} | {'SỐ ĐIỆN THOẠI':<15} | {'PHÒNG BAN':<10}")
        print("-" * 75)
        
        for item in employee_list:
            # Tách các trường thông tin của nhân viên hiện tại
            info = item.split(";")
            
            # Chuẩn hóa dữ liệu chữ
            emp_id = info[0].strip().upper()
            full_name = info[1].strip().title()
            department = info[3].strip().upper()
            
            # Xử lý làm sạch số điện thoại (Xóa các dấu gạch ngang '-')
            raw_phone = info[2].strip()
            clean_phone = ""
            for char in raw_phone:
                if char != "-":
                    clean_phone += char
                    
            # Đánh giá tính hợp lệ của số điện thoại sau khi làm sạch
            # SĐT hợp lệ phải toàn bộ là số và thường có độ dài là 10 ký tự
            if clean_phone.isdigit() and len(clean_phone) == 10:
                # Che 6 số đầu bằng dấu ******, giữ lại 4 số cuối bằng slicing [-4:]
                formatted_phone = "******" + clean_phone[-4:]
            else:
                formatted_phone = "Invalid Format"
                
            # In dòng dữ liệu đã căn lề ngay ngắn vào bảng
            print(f"{emp_id:<10} | {full_name:<20} | {formatted_phone:<15} | {department:<10}")
            
        print("-" * 75 + "\n")
        
    # --- CHỨC NĂNG 3: Tìm kiếm nhân viên theo mã ID ---
    elif choice == "3":
        # Nhập ID cần tìm, xử lý xóa khoảng trắng và chuyển chữ hoa để khớp bộ lọc
        search_id = input("Nhập mã nhân viên cần tìm (Ví dụ: emp-002): ").strip().upper()
        
        # Biến cờ hiệu kiểm tra trạng thái tìm kiếm (False là không thấy)
        is_found = False
        
        # Tách danh sách để duyệt tìm kiếm cuốn chiếu
        employee_list = raw_data.split("|")
        
        for item in employee_list:
            info = item.split(";")
            current_id = info[0].strip().upper()
            
            # Nếu trùng khớp mã ID cần tìm
            if current_id == search_id:
                is_found = True
                
                # Tiến hành chuẩn hóa để hiển thị riêng hồ sơ nhân viên này
                full_name = info[1].strip().title()
                department = info[3].strip().upper()
                
                # Làm sạch SĐT tương tự như chức năng 2
                raw_phone = info[2].strip()
                clean_phone = ""
                for char in raw_phone:
                    if char != "-":
                        clean_phone += char
                        
                if clean_phone.isdigit() and len(clean_phone) == 10:
                    formatted_phone = "******" + clean_phone[-4:]
                else:
                    formatted_phone = "Invalid Format"
                    
                # Xuất kết quả tìm thấy
                print(f"\n[THÔNG TIN NHÂN VIÊN ĐƯỢC TÌM THẤY]:")
                print(f" - Mã nhân viên: {current_id}")
                print(f" - Họ và tên   : {full_name}")
                print(f" - Số điện thoại: {formatted_phone}")
                print(f" - Phòng ban   : {department}\n")
                break # Tìm thấy rồi thì ngắt vòng lặp tìm kiếm ngay
                
        # Sau khi duyệt hết danh sách mà cờ hiệu vẫn là False
        if is_found == False:
            print("=> Không tìm thấy nhân viên\n")
            
    # --- CHỨC NĂNG 4: Thoát chương trình ---
    elif choice == "4":
        print("Thoát chương trình!")
        print("Hệ thống quản lý dữ liệu nhân sự đã đóng an toàn.")
        break # Bẻ gãy vòng lặp vô hạn
        
    # --- XỬ LÝ BẪY 3: Lựa chọn sai trên menu điều hướng ---
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!\n")