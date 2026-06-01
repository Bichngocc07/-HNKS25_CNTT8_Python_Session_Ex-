print("==================================================")
print("        HỆ THỐNG IN SƠ ĐỒ CHỖ HỌC - BACKEND")
print("==================================================")

room_count = int(input("Nhập số lượng phòng học cần kiểm tra: "))

if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
    print("======= CHƯƠNG TRÌNH KẾT THÚC =======")
else:
    for i in range(1, room_count + 1):
        print(f"\n--- ĐANG XỬ LÝ PHÒNG HỌC THỨ {i} ---")
        
        rows = int(input("Nhập số hàng ghế của từng phòng: "))
        seats_per_row = int(input("Nhập số ghế trên mỗi hàng: "))
        
        if rows > 12 or seats_per_row > 12:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break
            
        if rows <= 0 or seats_per_row <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            print("-" * 40)
            continue
            
        print("\nSơ đồ chỗ ngồi của phòng:")
        for r in range(0, rows):
            for s in range(0, seats_per_row):
                print("*", end="")
            print("")
            
        print("-" * 40)

    print("\n======= TIẾN TRÌNH KẾT THÚC =======")
