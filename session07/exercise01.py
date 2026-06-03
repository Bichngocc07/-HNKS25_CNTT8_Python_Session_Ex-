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

    if choice == "2":
        parts = raw_input.split(";")
        raw_name = parts[0]
        raw_year = parts[1]

        clean_name = raw_name.strip().title()

        clean_year = int(raw_year.strip())
        current_age = 2026 - clean_year

        # Hiển thị kết quả sau khi xử lý sạch dữ liệu
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

        first_name = name_words[0].lower()     
        middle_name = name_words[1].lower()    
        last_name = name_words[-1].lower()      

        email_username = last_name + first_name[0] + middle_name[0]
        generated_email = f"{email_username}@company.com"

        id_letters = last_name.upper()
        id_digits = raw_year[-2:]  
        generated_id = f"{id_letters}{id_digits}"

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
        print("Tạm biệt và hẹn gặp lại!")
        break 

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!\n")
