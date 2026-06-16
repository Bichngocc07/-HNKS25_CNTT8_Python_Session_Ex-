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
        print("-" * 37) 
        
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
    print("4. Thoát chương trình                ") 
    print("=====================================")

    choice = input("Mời bạn chọn chức năng (1-4) : ").strip()
    
    if choice == "1":
        xem_sanpham(products_list) 
    elif choice == "2":
        them_sanpham(products_list) 
    elif choice == "3":
        capnhat_gia(products_list) 
    elif choice == "4":      
        print("ĐÃ THOÁT CHƯƠNG TRÌNH !")
        break 
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 4.")
