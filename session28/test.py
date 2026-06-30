class Product:
    def __init__(self, id, name, price, quantity_sold, discount):
        self.id = id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount

        self.total_revenue = 0.0
        self.revenue_type = ""

        self.calculate_revenue()
        self.classify_revenue()

    def calculate_revenue(self):
        """Tính tổng doanh thu = Giá bán * Số lượng bán - Giảm giá."""
        revenue = (self.price * self.quantity_sold) - self.discount
        self.total_revenue = max(0.0, revenue)  

    def classify_revenue(self):
        """Phân loại doanh thu dựa trên mức tiền đạt được."""
        if self.total_revenue < 5000000:
            self.revenue_type = "Thấp"
        elif self.total_revenue < 20000000:
            self.revenue_type = "Trung bình"
        elif self.total_revenue < 50000000:
            self.revenue_type = "Khá"
        else:
            self.revenue_type = "Cao"


class ProductManager:
    def __init__(self):
        self.products = []

    def show_all(self):
        """Chức năng 1: Hiển thị toàn bộ danh sách sản phẩm dưới dạng bảng."""
        if not self.products:
            print("\nDanh sách sản phẩm đang rỗng!")
            return

        print("\n" + "="*42 + " DANH SÁCH SẢN PHẨM " + "="*43)
        print(f"{'Mã SP':<10}{'Tên sản phẩm':<25}{'Giá bán':<15}{'SL bán':<10}{'Giảm giá':<15}{'Doanh thu':<15}{'Phân loại':<15}")
        print("-" * 105)
        for p in self.products:
            print(f"{p.id:<10}{p.name:<25}{p.price:<15,.0f}{p.quantity_sold:<10}{p.discount:<15,.0f}{p.total_revenue:<15,.0f}{p.revenue_type:<15}")
        print("=" * 105)

    def load_test_data(self):
        """Hàm phụ trợ đẩy trước dữ liệu mẫu từ đề bài vào hệ thống."""
        self.products.append(Product("SP001", "Laptop Dell", 15000000, 3, 2000000))
        self.products.append(Product("SP002", "Chuột Logitech", 350000, 20, 500000))
        self.products.append(Product("SP003", "Bàn phím cơ AKKO", 1200000, 10, 1000000))
        self.products.append(Product("SP004", "Màn hình Samsung", 4500000, 5, 0))
        self.products.append(Product("SP005", "Tai nghe Sony", 2500000, 1, 0))


def main():
    manager = ProductManager()
    manager.load_test_data()

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
            manager.show_all()
        elif choice == "2":
            manager.add_product()
        elif choice == "3":
            manager.update_product()
        elif choice == "4":
            manager.delete_product()
        elif choice == "5":
            manager.search_product()
        elif choice == "6":
            print("ĐÃ THOÁT CHƯƠNG TRÌNH !")
            break
        else:
            print("LỰA CHỌN KHÔNG HỢP LỆ. VUI LÒNG THỬ LẠI SAU")


if __name__ == "__main__":
    main()
