products_list = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def xem_sanpham(products_list):
    print("----HIỂN THỊ DANH SÁCH SẢN PHẨM-----")
        
    if len(products_list) == 0:
        print("KHÔNG CÓ SẢN PHẨM NÀO")
    else:
        print(f"{'ID':<6} | {'Tên sản phẩm':<15} | {'Giá bán':<10}")
        print("-" * 37) # In đường kẻ phân cách
        
        for sp in products_list:
            print(f"{sp['id']:<6} | {sp['name']:<15} | {sp['price']:<10}")

def them_sanpham(products_list):
    print("-------- THÊM SẢN PHẨM MỚI ----------")


while True:
    print("=====================================")
    print("   QUẢN LÝ CỬA HÀNG - MINI STORE     ")
    print("=====================================")
    print("1. Xem danh sách sản phẩm hiện có    ")
    print("2. Thêm mới một sản phẩm             ")
    print("3. Cập nhật giá sản phẩm theo ID     ")
    print("4. Thoát chương trình                ") # Sửa đổi chữ từ text của bạn cho rõ ràng
    print("=====================================")

    # Nhận lựa chọn và dùng .strip() để xóa khoảng trắng thừa
    choice = input("Mời bạn chọn chức năng (1-4) : ").strip()
    
    if choice == "1":
        xem_sanpham(products_list) # Truyền biến toàn cục 'products' vào hàm
    elif choice == "2":
        them_sanpham(products_list) # Truyền biến toàn cục 'products' vào hàm
    elif choice == "3":
        capnhat_gia(products_list) # Gọi hàm cập nhật giá vừa viết thêm
    elif choice == "4":       # SỬA LỖI: Đề bài yêu cầu số 4 là thoát chương trình thay vì số 8
        print("ĐÃ THOÁT CHƯƠNG TRÌNH !")
        break # Bẻ gãy vòng lặp while True để dừng chương trình
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 4.")