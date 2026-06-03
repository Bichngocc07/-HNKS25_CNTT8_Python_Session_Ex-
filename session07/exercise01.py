raw_input = "   nGuyen vaN aN ; 2004   "

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
    if choice == "2":
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

        clean_name = raw_name.title()

        # Tách chuỗi tên thành danh sách các từ để bóc tách Họ, Tên đệm, Tên chính
        name_words = raw_name.split()

        # Chuyển toàn bộ về chữ viết thường để xử lý cấu trúc Email
        first_name = name_words[0].lower()       # Ví dụ: "nguyen"
        middle_name = name_words[1].lower()      # Ví dụ: "van"
        last_name = name_words[-1].lower()       # Ví dụ: "an"

        # 1. Tạo Email: Tên chính + chữ cái đầu của Họ + chữ cái đầu của Tên đệm
        # Ví dụ: "an" + "n" + "v" -> "annv" ghép với đuôi công ty
        email_username = last_name + first_name[0] + middle_name[0]
        generated_email = f"{email_username}@company.com"

        # 2. Tạo Mã ID: Viết hoa Tên chính + 2 số cuối năm sinh bằng kỹ thuật cắt chuỗi (Slicing)
        # Ví dụ: "AN" + "04" -> "AN04"
        id_letters = last_name.upper()
        id_digits = raw_year[-2:]  # Lấy 2 ký tự cuối cùng của chuỗi năm sinh
        generated_id = f"{id_letters}{id_digits}"

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
        print("Tạm biệt và hẹn gặp lại!")
        break  # Bẻ gãy vòng lặp while True để kết thúc

    # --- XỬ LÝ NGOẠI LỆ: Người dùng nhập sai số hoặc ký tự lạ ngoài menu ---
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!\n")
