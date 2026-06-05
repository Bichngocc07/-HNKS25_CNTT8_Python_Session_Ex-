cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]
print("===========================================================")
print("               SHOPEE CART MANAGEMENT SYSTEM               ")
print("===========================================================")
print("1. Xem chi tiết giỏ hàng & Tính tổng tiền ")
print("2. Thêm sản phẩm mới / Cộng dồn số lượng ")
print("3. Cập nhật số lượng của một sản phẩm ")
print("4. Xóa sản phẩm khỏi giỏ hàng ")
print("5. Thoát chương trình ")
print("===========================================================")
choice = input ("Mời bạn chọn chức năng (1-5):")


# *** Chức năng 1: Xem chi tiết giỏ hàng và Tổng tiền

# In ra danh sách sản phẩm theo định dạng bảng trực quan.
# Tính và hiển thị tổng số lượng tất cả sản phẩm và tổng tiền của toàn bộ giỏ hàng
if choice == "1":
    print("\n--- CHI TIẾT GIỎ HÀNG ---")
    print("STT | Mã SP | Tên Sản Phẩm           | SL | Đơn Giá      | Thành Tiền")

    tong_sl = 0
    tong_tien = 0

    for i in range(len(cart_items)):
        ma_sp = cart_items[i][0]
        ten_sp = cart_items[i][1]
        sl = cart_items[i][2]
        don_gia = cart_items[i][3]

        thanh_tien = sl * don_gia

        tong_sl += sl
        tong_tien += thanh_tien

        print(f"{i+1:<3} | {ma_sp:<5} | {ten_sp:<22} | {sl:<2} | {don_gia:>10,}đ | {thanh_tien:>10,}đ")

    print("\n=> Tổng số lượng sản phẩm trong giỏ:", tong_sl)
    print("=> TỔNG TIỀN THANH TOÁN:", f"{tong_tien:,}đ")
#
#*** Chức năng 2: Thêm sản phẩm mới hoặc Tăng số lượng

# Hệ thống yêu cầu người dùng nhập: 
# - Mã sản phẩm
# - Tên sản phẩm
# - Số lượng
# - Đơn giá.
# Nếu Mã sản phẩm đã tồn tại trong giỏ hàng, hệ thống tự động cộng dồn số lượng mới nhập vào số lượng cũ (không tạo dòng mới). 
# Nếu Mã sản phẩm chưa tồn tại, thêm mới một sản phẩm [Mã, Tên, Số lượng, Đơn giá] vào cuối danh sách.
if choice == "2":
    ma_sp = input("Nhập mã sản phẩm: ")
    ten_sp = input("Nhập tên sản phẩm: ")
    so_luong = int(input("Nhập số lượng: "))
    don_gia = int(input("Nhập đơn giá: "))

    tim_thay = False

    for item in cart_items:
        if item[0] == ma_sp:
            item[2] += so_luong  # cộng dồn số lượng
            tim_thay = True
            print("Sản phẩm đã tồn tại. Đã cập nhật số lượng!")
            break

    if not tim_thay:
        cart_items.append([ma_sp, ten_sp, so_luong, don_gia])
        print("Thêm sản phẩm mới thành công!")
# *** Chức năng 3: Cập nhật số lượng sản phẩm

# Người dùng nhập Mã sản phẩm và Số lượng mới cần thay đổi.
# Tìm kiếm sản phẩm theo Mã. Nếu tìm thấy, cập nhật lại số lượng bằng số lượng mới nhập.
elif choice == "3":
    ma_sp = input("Nhập mã sản phẩm cần cập nhật: ")
    so_luong_moi = int(input("Nhập số lượng mới: "))

    tim_thay = False

    for item in cart_items:
        if item[0] == ma_sp:
            item[2] = so_luong_moi
            tim_thay = True
            print("Cập nhật số lượng thành công!")
            break

    if not tim_thay:
        print("Không tìm thấy sản phẩm trong giỏ hàng!")
# *** Chức năng 4: Xóa sản phẩm khỏi giỏ hàng

# Người dùng nhập Mã sản phẩm muốn xóa.
# Tìm và xóa hoàn toàn sản phẩm đó.
elif choice == "4":
    ma_sp = input("Nhập mã sản phẩm cần xóa: ")

    tim_thay = False

    for item in cart_items:
        if item[0] == ma_sp:
            cart_items.remove(item)
            tim_thay = True
            print("Xóa sản phẩm thành công!")
            break

    if not tim_thay:
        print("Không tìm thấy sản phẩm trong giỏ hàng!")
# *** Chức năng 5: Thoát chương trình.
elif choice == "5":
    print("Cảm ơn bạn đã sử dụng chương trình!")
