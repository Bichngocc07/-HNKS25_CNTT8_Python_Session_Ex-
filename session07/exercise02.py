# Chuỗi dữ liệu thô ban đầu hệ thống nhận được
raw_input = "   nGuyen vaN aN ; 2004   "

# Vòng lặp chính duy trì menu điều hướng liên tục
while True:
    # Hiển thị menu chức năng của hệ thống
    print("===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    print("=====================================")
    
    # Nhận lựa chọn từ người dùng
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    print("")  # Xuống dòng cho thoáng giao diện
    
    # --- CHỨC NĂNG 1: Hiển thị chuỗi dữ liệu gốc ---
    if choice == "1":
        print("Chuỗi dữ liệu gốc hiện tại:")
        print(f"'{raw_input}'")
        print("\n" + "-"*40 + "\n")
        
    # --- CHỨC NĂNG 2: Chuẩn hóa Họ tên và tính Tuổi ---
    elif choice == "2":
        # Tách chuỗi họ tên và năm sinh dựa vào dấu chấm phẩy ';'
        parts = raw_input.split(";")
        raw_name = parts[0]
        raw_year = parts[1]
        
        # Loại bỏ khoảng trắng thừa và viết hoa chữ cái đầu từng từ (Title Case)
        clean_name = raw_name.strip().title()
        
        # Loại bỏ khoảng trắng của năm, ép kiểu số nguyên và tính tuổi theo mốc 2026
        clean_year = int(raw_year.strip())
        current_age = 2026 - clean_year
        
        # Hiển thị kết quả sau khi xử lý sạch dữ liệu
        print("[KẾT QUẢ CHUẨN HÓA DỮ LIỆU]:")
        print(f" - Họ và tên: {clean_name}")
        print(f" - Tuổi hiện tại: {current_age} tuổi")
        print("\n" + "-"*40 + "\n")
        
    # --- CHỨC NĂNG 3: Tạo Mã ID và Email tự động (In thẻ thành viên) ---
    elif choice == "3":
        # Tiến hành tách chuỗi thô tương tự chức năng 2
        parts = raw_input.split(";")
        raw_name = parts[0].strip()
        raw_year = parts[1].strip()
        
        # Định dạng họ tên viết hoa chuẩn để in lên thẻ
        clean_name = raw_name.title()
        
        # Tách chuỗi tên thành danh sách các từ để bóc tách Họ, Tên đệm, Tên chính
        name_words = raw_name.split()
        
        # Chuyển toàn bộ về chữ viết thường để xử lý cấu trúc Email
        ho_lowercase = name_words[0].lower()         # Ví dụ: "nguyen"
        dem_lowercase = name_words[1].lower()        # Ví dụ: "van"
        ten_lowercase = name_words[-1].lower()       # Ví dụ: "an"
        
        # 1. Tạo Email: Tên chính + chữ cái đầu của Họ [0] + chữ cái đầu của Tên đệm [0]
        # Sử dụng chỉ mục [0] để lấy ký tự đầu tiên của chuỗi
        ten_dang_nhap = ten_lowercase + ho_lowercase[0] + dem_lowercase[0]
        generated_email = f"{ten_dang_nhap}@company.com"
        
        # 2. Tạo Mã ID: Viết hoa Tên chính + 2 số cuối năm sinh bằng kỹ thuật cắt chuỗi (Slicing)
        id_chu = ten_lowercase.upper()
        id_so = raw_year[-2:]  # Lấy 2 ký tự cuối cùng của chuỗi năm sinh (ví dụ: "04")
        generated_id = f"{id_chu}{id_so}"
        
        # 3. Sử dụng f-string định dạng khung thẻ thành viên vuông vức
        print("-----------------------------------------")
        print("            THẺ THÀNH VIÊN MỚI           ")
        print("-----------------------------------------")
        print(f"Họ và tên : {clean_name}")
        print(f"Mã ID     : {generated_id}")
        print(f"Email     : {generated_email}")
        print("-----------------------------------------")
        print("\n" + "-"*40 + "\n")
        
    # --- CHỨC NĂNG 4: Thoát chương trình ---
    elif choice == "4":
        print("Chương trình đã dừng!")
        print("Tạm biệt và hẹn gập lại!")
        break  # Bẻ gãy vòng lặp while True để kết thúc
        
    # --- XỬ LÝ NGOẠI LỆ: Người dùng nhập sai ngoài menu ---
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại từ 1 đến 4!\n")