class Product:
    def __init__(self,id,name,price,quantity_sold,discount):
        self.id = id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount

        self.total_revenue = 0.0
        self.revenue_type = ""

        self.calculate_revenue()
        self.classify_revenue()
class ProductManager:
    def __init__(self):
        self.products = []

def show_all(self):
        """Chức năng 1: Hiển thị toàn bộ danh sách sản phẩm dưới dạng bảng."""
        if not self.products:
            print("\n Danh sách sản phẩm đang rỗng!")
            return

        print("\n" + "="*50 + " DANH SÁCH SẢN PHẨM " + "="*50)
        print(f"{'Mã SP':<10}{'Tên sản phẩm':<25}{'Giá bán':<15}{'SL bán':<10}{'Giảm giá':<15}{'Doanh thu':<15}{'Phân loại':<15}")
        print("-" * 105)
        for p in self.products:
            print(f"{p.id:<10}{p.name:<25}{p.price:<15,.0f}{p.quantity_sold:<10}{p.discount:<15,.0f}{p.total_revenue:<15,.0f}{p.revenue_type:<15}")
        print("=" * 105)
 
while True:
    print("================ MENU ================")
    print("1. Hiển thị danh sách sản phẩm        ")
    print("2. Thêm sản phẩm mới                  ")
    print("3. Cập nhật sản phẩm                  ")
    print("4. Xóa sản phẩm                       ")
    print("5. Tìm kiếm sản phẩm                  ")
    print("6. Thoát                              ")
    print("======================================")
    choice = input("Nhập lựa chọn của bạn: ").strip()
    if choice == "1":
        show_all()
    elif choice == "2":
        add_product()
    elif choice == "3":
        update_product()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        search_product()
    elif choice == "6":
        print("ĐÃ THOÁT CHƯƠNG TRÌNH !")
        break
    else:
        print("LỰA CHỌN KHÔNG HỢP LỆ. VUI LÒNG THỬ LẠI SAU")
if __name__ == "__main__":
    main()