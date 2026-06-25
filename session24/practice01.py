# =============================================================================
# HỆ THỐNG QUẢN LÝ HÓA ĐƠN RIKKEI COFFEE (CHUẨN PRODUCTION OOP)
# =============================================================================

class CoffeeOrder:
    # Thuộc tính cấp lớp (Class Attribute) quản lý mức thuế dùng chung toàn hệ thống
    _vat_rate = 0.10  # Mặc định ban đầu là 10%

    def __init__(self, table_number):
        """Khởi tạo hóa đơn mới cho từng bàn ăn."""
        self.table_number = table_number
        # Áp dụng tính Đóng gói: Biến thuộc tính tổng tiền thành thuộc tính ẩn (Private)
        self.__total_amount = 0

    # -------------------------------------------------------------------------
    # CƠ CHẾ KIỂM SOÁT ĐÓNG GÓI (GETTER / PROPERTY)
    # -------------------------------------------------------------------------
    @property
    def total_amount(self):
        """Decorator cấp quyền CẤP CHỈ ĐỌC (Read-only) cho thuộc tính tổng tiền."""
        return self.__total_amount

    # -------------------------------------------------------------------------
    # CÁC PHƯƠNG THỨC NGHIỆP VỤ (INSTANCE METHODS)
    # -------------------------------------------------------------------------
    def add_item(self, price, quantity):
        """Thêm món vào hóa đơn với kiểm tra tính hợp lệ dữ liệu đầu vào."""
        try:
            # Ép kiểu dữ liệu để phòng ngừa lỗi bẩn từ API POS
            item_price = float(price)
            item_qty = int(quantity)

            if item_price < 0 or item_qty < 0:
                print("⚠️ Lỗi nghiệp vụ: Giá tiền và số lượng không được nhỏ hơn 0!")
                return

            # Tăng tổng tiền hóa đơn an toàn bên trong lớp
            self.__total_amount += item_price * item_qty

        except ValueError:
            print("⚠️ Lỗi hệ thống: Định dạng số liệu món ăn không hợp lệ!")

    def calculate_final_bill(self):
        """Tính toán tổng hóa đơn cuối cùng đã bao gồm cả thuế suất VAT hiện hành."""
        # Gọi chính xác giá trị thuế đang áp dụng ở cấp lớp thông qua Class Attribute
        final_bill = self.__total_amount * (1 + CoffeeOrder._vat_rate)
        return round(final_bill, 2)

    # -------------------------------------------------------------------------
    # PHƯƠNG THỨC ĐỒNG BỘ TOÀN CỤC (CLASS METHOD)
    # -------------------------------------------------------------------------
    @classmethod
    def update_vat_rate(cls, new_rate):
        """
        Phương thức lớp giúp cập nhật đồng bộ thuế VAT cho toàn bộ hệ thống.
        Thay thế hoàn toàn lỗi nhầm lẫn Instance Method cũ.
        """
        try:
            rate_val = float(new_rate)
            if 0 <= rate_val <= 1:
                cls._vat_rate = rate_val
                # Sử dụng hàm print() chính quy thông báo tiến trình
                print(f"[HỆ THỐNG] Thay đổi mức thuế VAT toàn hệ thống thành: {rate_val * 100}%")
            else:
                print("⚠️ Lỗi: Thuế suất VAT phải nằm trong khoảng từ 0.0 đến 1.0!")
        except ValueError:
            print("⚠️ Lỗi: Định dạng mức thuế mới không hợp lệ!")

    @classmethod
    def get_vat_rate(cls):
        """Lấy thông tin mức thuế hiện tại của hệ thống."""
        return cls._vat_rate


# =============================================================================
# VÒNG LẶP KIỂM THỬ KỊCH BẢN CHẠY THỰC TẾ
# =============================================================================
def main():
    print("====== KÍCH HOẠT HỆ THỐNG QUẢN LÝ POS RIKKEI COFFEE ======")

    # 1. Khởi tạo 2 hóa đơn cho Bàn 5 và Bàn 2
    order_table5 = CoffeeOrder("Bàn 5")
    order_table2 = CoffeeOrder("Bàn 2")

    # 2. Khách hàng tại các bàn tiến hành gọi món
    order_table5.add_item(35000, 2)  # Gọi 2 ly Phin Sữa Đá
    order_table2.add_item(45000, 1)  # Gọi 1 ly Trà Sen Vàng

    # 3. THỬ NGHIỆM BẪY BẢO MẬT: Đối tượng xấu bên ngoài cố tình can thiệp trực tiếp dữ liệu
    print("\n--- Chặng 1: Thử nghiệm bẫy can thiệp dữ liệu Đóng gói ---")
    try:
        # Lệnh này sẽ quăng lỗi AttributeError vì thuộc tính __total_amount đã bị khóa chỉ đọc
        order_table5.total_amount = 0
    except AttributeError:
        print("🛡️ [BẢO MẬT] Chặn thành công hành vi can thiệp sửa đổi trái phép Tổng tiền!")

    # 4. THỬ NGHIỆM ĐỒNG BỘ THẾ: Quản lý cập nhật mức thuế toàn chuỗi xuống 8% (0.08)
    print("\n--- Chặng 2: Thử nghiệm đồng bộ hóa dữ liệu Thuế suất ---")
    # Gọi hàm cấp lớp (Class Method) chuẩn chỉnh
    CoffeeOrder.update_vat_rate(0.08)

    # 5. Xuất báo cáo kết quả tài chính cuối cùng lên màn hình Console
    print("\n--- BÁO CÁO DOANH THU HOÀN THÀNH ---")
    print(f"Tổng tiền Bàn 5 (Sau VAT): {order_table5.calculate_final_bill():,} VNĐ")
    print(f"Tổng tiền Bàn 2 (Sau VAT): {order_table2.calculate_final_bill():,} VNĐ")
    
    print(f"Mức thuế đang áp dụng cho hóa đơn Bàn 5: {order_table5.get_vat_rate() * 100}%")
    print(f"Mức thuế đang áp dụng cho hóa đơn Bàn 2: {order_table2.get_vat_rate() * 100}%")
    print("==========================================================")


if __name__ == "__main__":
    main()