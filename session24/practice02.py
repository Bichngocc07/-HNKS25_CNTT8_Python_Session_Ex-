# =============================================================================
# HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE (CHUẨN PRODUCTION OOP)
# =============================================================================

class MemberCard:
    def __init__(self, customer_name, points=0):
        """Khởi tạo thông tin thẻ thành viên của khách hàng."""
        self.customer_name = customer_name
        
        # Áp dụng Name Mangling: Biến thuộc tính points thành private (__points)
        # để bảo vệ dữ liệu, không cho phép can thiệp tự do từ bên ngoài
        self.__points = 0
        
        # Gọi setter để kiểm tra dữ liệu đầu vào ngay khi khởi tạo thẻ
        self.points = points

    # -------------------------------------------------------------------------
    # CƠ CHẾ ĐÓNG GÓI VÀ KIỂM SOÁT TOÀN VẸN DỮ LIỆU (GETTER / SETTER)
    # -------------------------------------------------------------------------
    @property
    def points(self):
        """Getter: Cho phép các bộ phận khác bên ngoài đọc số điểm hiện tại."""
        return self.__points

    @points.setter
    def points(self, new_points):
        """
        Setter: Bộ lọc thông minh kiểm soát hành vi gán/sửa điểm số.
        Chặn đứng lỗi nhập chữ hoặc nhập số điểm âm.
        """
        try:
            # Kiểm tra lỗi ép kiểu nếu đầu vào bị bẩn (Dirty Data)
            points_val = int(new_points)
            
            # Chặn lỗi nghiệp vụ số điểm nhỏ hơn 0
            if points_val < 0:
                print("⚠️ Lỗi nghiệp vụ: Số điểm tích lũy không được nhỏ hơn 0!")
                return
            
            # Nếu vượt qua chặng kiểm tra an toàn, tiến hành gán dữ liệu thực tế
            self.__points = points_val
            
        except (ValueError, TypeError):
            print("⚠️ Lỗi hệ thống: Số điểm nhập vào không hợp lệ! Không phải số nguyên.")

    # -------------------------------------------------------------------------
    # PHƯƠNG THỨC NGHIỆP VỤ CỦA ĐỐI TƯỢNG (INSTANCE METHOD)
    # -------------------------------------------------------------------------
    def add_points(self, amount):
        """Cộng thêm điểm thưởng tích lũy cho khách hàng khi mua sắm thành công."""
        try:
            added_val = int(amount)
            if added_val <= 0:
                print("⚠️ Lỗi: Số điểm cộng thêm phải lớn hơn 0!")
                return
            
            # Cộng dồn an toàn thông qua việc gán trực tiếp vào biến private nội bộ
            self.__points += added_val
            
        except (ValueError, TypeError):
            print("⚠️ Lỗi: Định dạng điểm cộng thêm không hợp lệ!")

    # -------------------------------------------------------------------------
    # PHƯƠNG THỨC TIỆN ÍCH TĨNH (STATIC METHOD) - KHÔNG CẦN SELF
    # -------------------------------------------------------------------------
    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        """
        Phương thức tĩnh kiểm tra điều kiện tặng Voucher dựa trên giá trị hóa đơn.
        Hàm hoạt động độc lập, không cần khởi tạo thực thể đối tượng (No self).
        """
        try:
            bill_val = float(bill_amount)
            # Quy định: Hóa đơn từ 200,000 VNĐ trở lên sẽ được tặng voucher
            return bill_val >= 200000
        except (ValueError, TypeError):
            print("⚠️ Lỗi: Định dạng số tiền hóa đơn không hợp lệ!")
            return False


# =============================================================================
# KỊCH BẢN CHẠY KIỂM THỬ THỰC TẾ HỆ THỐNG
# =============================================================================
def main():
    print("====== KÍCH HOẠT KIỂM TRA TOÀN VẸN DỮ LIỆU RIKKEI COFFEE ======")

    # 1. Khởi tạo một thẻ thành viên hợp lệ
    card1 = MemberCard("Lê Văn C", 50)
    print(f"Khách hàng: {card1.customer_name} | Số điểm khởi tạo thành công: {card1.points}")

    # 2. THỬ NGHIỆM BẪY LỖI 1: Thu ngân gõ nhầm điểm số là chữ hoặc số âm
    print("\n--- Chặng 1: Thử nghiệm bẫy dữ liệu điểm số không hợp lệ ---")
    card1.points = -10       # Thử gán số âm
    card1.points = "mười"    # Thử gán chuỗi chữ bẩn
    print(f"-> Số điểm hiện tại sau các hành vi gán lỗi: {card1.points} (Giữ nguyên, không bị phá hoại)")

    # 3. THỬ NGHIỆM BẪY LỖI 2: Đối tượng xấu cố tình can thiệp trực tiếp dữ liệu công khai từ bên ngoài
    print("\n--- Chặng 2: Thử nghiệm chặn hành vi can thiệp sửa đổi trực tiếp ---")
    try:
        # Lệnh này sẽ báo lỗi AttributeError vì thuộc tính __points đã được giấu bọc an toàn
        card1.points = 0
        # Nếu cố tình can thiệp bằng biến ẩn danh card1.__points = 0, Python sẽ tự hiểu là một biến độc lập 
        # nhờ cơ chế Name Mangling, không làm ảnh hưởng tới thuộc tính ẩn gốc.
    except AttributeError:
        print("🛡️ [BẢO MẬT] Hệ thống khóa chặn thành công hành vi sửa đổi điểm tự do!")

    # 4. THỬ NGHIỆM BIẾN ĐỔI CHỨC NĂNG VOUCHER (STATIC METHOD)
    print("\n--- Chặng 3: Kiểm tra tính năng xác thực Voucher thông qua Static Method ---")
    bill_1 = 250000
    bill_2 = 150000

    # Điểm đặc biệt: Có thể gọi trực tiếp từ Tên Lớp Class mà không cần tạo đối tượng hay truyền self
    result_bill1 = MemberCard.is_eligible_for_voucher(bill_1)
    result_bill2 = MemberCard.is_eligible_for_voucher(bill_2)

    print(f" + Hóa đơn {bill_1:,} VNĐ -> Đạt điều kiện tặng Voucher: {result_bill1}")
    print(f" + Hóa đơn {bill_2:,} VNĐ -> Đạt điều kiện tặng Voucher: {result_bill2}")
    print("=====================================================================")


if __name__ == "__main__":
    main()