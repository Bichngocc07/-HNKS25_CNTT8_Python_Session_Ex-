raw_input = "   nGuyen vaN aN ; 2004   "

while True:
    print("===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    print("") 
    
    if choice == "1":
        print("Chuỗi dữ liệu gốc hiện tại:")
        print(f"'{raw_input}'")
        print("\n" + "-"*40 + "\n")
        
    elif choice == "2":
        parts = raw_input.split(";")
        raw_name = parts[0]
        raw_year = parts[1]
        
        clean_name = raw_name.strip().title()
        
        clean_year = int(raw_year.strip())
        current_age = 2026 - clean_year
        
        print("[KẾT QUẢ CHUẨN HÓA DỮ LIỆU]:")
        print(f" - Họ và tên: {clean_name}")
        print(f" - Tuổi hiện tại: {current_age} tuổi")
        print("\n" + "-"*40 + "\n")
        
    elif choice == "3":
        parts = raw_input.split(";")
        raw_name = parts[0].strip()
        raw_year = parts[1].strip()
        
        clean_name = raw_name.title()
        
        name_words = raw_name.split()
        
        ho_lowercase = name_words[0].lower()       
        dem_lowercase = name_words[1].lower()      
        ten_lowercase = name_words[-1].lower()    
        
        ten_dang_nhap = ten_lowercase + ho_lowercase[0] + dem_lowercase[0]
        generated_email = f"{ten_dang_nhap}@company.com"
        
        id_chu = ten_lowercase.upper()
        id_so = raw_year[-2:]  
        generated_id = f"{id_chu}{id_so}"
        
        print("-----------------------------------------")
        print("            THẺ THÀNH VIÊN MỚI           ")
        print("-----------------------------------------")
        print(f"Họ và tên : {clean_name}")
        print(f"Mã ID     : {generated_id}")
        print(f"Email     : {generated_email}")
        print("-----------------------------------------")
        print("\n" + "-"*40 + "\n")
        
    elif choice == "4":
        print("Chương trình đã dừng!")
        print("Tạm biệt và hẹn gập lại!")
        break 
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại từ 1 đến 4!\n")
