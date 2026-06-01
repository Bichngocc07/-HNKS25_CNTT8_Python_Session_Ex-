print("==================================================")
print("        HỆ THỐNG IN SƠ ĐỒ CHỖ HỌC - BACKEND")
print("==================================================")

# Nhập số lượng phòng học cần kiểm tra
room_count = int(input("Nhập số lượng phòng học cần kiểm tra: "))

# BẪY 1: Kiểm tra số lượng phòng học không hợp lệ
if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
    print("======= CHƯƠNG TRÌNH KẾT THÚC =======")
else:
    # Vòng lặp ngoài cùng: Duyệt qua từng phòng học
    for i in range(1, room_count + 1):
        print(f"\n--- ĐANG XỬ LÝ PHÒNG HỌC THỨ {i} ---")
        
        # Nhập số hàng và số ghế
        rows = int(input("Nhập số hàng ghế của từng phòng: "))
        seats_per_row = int(input("Nhập số ghế trên mỗi hàng: "))
        
        # BẪY 3: Kiểm tra phòng quá lớn (lớn hơn 12)
        if rows > 12 or seats_per_row > 12:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            # Dừng ngay toàn bộ chương trình kiểm tra phòng học
            break
            
        # BẪY 2: Kiểm tra số hàng hoặc số ghế không hợp lệ (nhỏ hơn hoặc bằng 0)
        if rows <= 0 or seats_per_row <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            print("-" * 40)
            # Bỏ qua tiến trình vẽ, chuyển sang xử lý phòng học tiếp theo
            continue
            
        # TIẾN TRÌNH VẼ SƠ ĐỒ CHỖ NGỒI (Sử dụng Vòng lặp lồng nhau - Nested Loop)
        print("\nSơ đồ chỗ ngồi của phòng:")
        for r in range(0, rows):
            # Vòng lặp con bên trong đảm nhiệm in các dấu * trên cùng 1 hàng
            for s in range(0, seats_per_row):
                print("*", end="")
            # Sau khi in xong một hàng ghế, dùng lệnh print rỗng để xuống dòng
            print("")
            
        print("-" * 40)

    print("\n======= TIẾN TRÌNH KẾT THÚC =======")