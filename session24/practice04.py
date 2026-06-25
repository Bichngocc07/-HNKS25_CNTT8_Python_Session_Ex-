import re

# =============================================================================
# 1. ĐỊNH NGHĨA LỚP MEMBERCARD (HỆ THỐNG QUẢN LÝ THẺ THÀNH VIÊN OOP)
# =============================================================================
class MemberCard:
    # Thuộc tính cấp lớp (Class Attribute): Tỷ giá quy đổi điểm mặc định (1 điểm = 1,000 VNĐ)
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        """Khởi tạo một tài khoản thẻ thành viên mới."""
        self.card_id = card_id
        self.name = name
        # Áp dụng Đóng gói bảo mật: Giấu thuộc tính điểm bằng cơ chế Private (__points)
        self.__points = 0
        self.tier = "Standard"

    # -------------------------------------------------------------------------
    # CƠ CHẾ ĐÓNG GÓI - CHỈ CẤP QUYỀN ĐỌC ĐIỂM (GETTER / PROPERTY)
    # -------------------------------------------------------------------------
    @property
    def points(self):
        """Property giúp lấy số điểm hiện tại ra xem (Read-only). Không có Setter."""
        return self.__points

    # -------------------------------------------------------------------------
    # PHƯƠNG THỨC TIỆN ÍCH TĨNH (STATIC METHOD) - KIỂM TRA ĐỊNH DẠNG MÃ THẺ
    # -------------------------------------------------------------------------
    @staticmethod
    def is_valid_card_id(card_id):
        """
        Bẫy 2: Kiểm tra xem mã thẻ nhập vào có đúng chuẩn: RC + 2 chữ số hay không.
        Trả về True nếu hợp lệ, False nếu sai định dạng.
        """
        # Sử dụng Biểu thức chính quy (Regular Expression) để quét chuỗi
        pattern = r"^RC\d{2}$"
        if re.match(pattern, card_id):
            return True
        return False

    # -------------------------------------------------------------------------
    # PHƯƠNG THỨC LỚP (CLASS METHOD) - CẬP NHẬT TỶ GIÁ TOÀN CHUỖI
    # -------------------------------------------------------------------------
    @classmethod
    def update_point_value(cls, new_value):
        """Chức năng 5: Cập nhật tỷ giá quy đổi tiền của 1 điểm cho toàn hệ thống."""
        try:
            val = int(new_value)
            if val <= 0:
                print("⚠️ Lỗi: Giá trị quy đổi điểm phải lớn hơn 0 VNĐ!")
                return False
            cls.point_value_vnd = val
            return True
        except ValueError:
            print("⚠️ Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
            return False

    # -------------------------------------------------------------------------
    # CÁC PHƯƠNG THỨC NGHIỆP VỤ ĐỐI TƯỢNG (INSTANCE METHODS)
    # -------------------------------------------------------------------------
    def earn_points(self, bill_amount):
        """Chức năng 3: Tính toán tích điểm tự động dựa trên hóa đơn mua hàng."""
        try:
            bill = int(bill_amount)
            if bill <= 0:
                print("⚠️ Lỗi: Giá trị hóa đơn mua hàng phải lớn hơn 0!")
                return
            
            # Quy tắc tích lũy: Cứ mỗi 10,000 VNĐ hóa đơn tính được 1 điểm (lấy phần nguyên)
            new_earned_points = bill // 10000
            self.__points += new_earned_points
            
            print(f"Khách hàng: {self.name}")
            print(f"Hóa đơn: {bill:,} VNĐ")
            print(f"Số điểm được tích: {new_earned_points}")
            print(f"Tổng điểm hiện tại: {self.__points}")
            
            # Luồng xử lý tự động nâng hạng thẻ lên VIP khi tích lũy đạt từ 100 điểm trở lên
            if self.__points >= 100 and self.tier != "VIP":
                self.tier = "VIP"
                print("🎉 Chúc mừng! Khách hàng đã được nâng hạng lên VIP.")
                
            print(f"Hạng thẻ hiện tại: {self.tier}")
            
        except ValueError:
            print("⚠️ Lỗi: Giá trị hóa đơn đầu vào phải là số!")

    def redeem_points(self, points_to_use):
        """Chức năng 4: Khách hàng dùng điểm đổi giảm trừ trực tiếp vào hóa đơn."""
        try:
            pts = int(points_to_use)
            
            # Bẫy 3: Kiểm tra tính hợp lệ của số điểm muốn tiêu
            if pts <= 0:
                print("⚠️ Thao tác thất bại: Số điểm muốn sử dụng phải lớn hơn 0!")
                return
            
            if pts > self.__points:
                print("❌ Không thể đổi điểm!")
                print(f"Số điểm muốn sử dụng vượt quá số điểm hiện có.")
                print(f"Điểm hiện tại của khách: {self.__points}")
                print(f"Biến số điểm giữ nguyên.")
                print(f"Số điểm sau giao dịch: {self.__points}")
                return

            # Thực hiện trừ số điểm tiêu và tính toán tiền giảm giá dựa vào tỷ giá cấp lớp
            self.__points -= pts
            discount_amount = pts * MemberCard.point_value_vnd
            
            print(f"Đã trừ {pts} điểm. Khách hàng được giảm giá {discount_amount:,} VNĐ vào hóa đơn!")
            print(f"Số điểm còn lại: {self.__points}")
            print(f"Hạng thẻ hiện tại: {self.tier}")
            
        except ValueError:
            print("⚠️ Lỗi: Số điểm muốn sử dụng phải là số nguyên!")


# =============================================================================
# 2. VÒNG LẶP ĐIỀU KHIỂN CHƯƠNG TRÌNH CHÍNH (MAIN CONSOLE LOOP)
# =============================================================================
def main():
    # Sử dụng Dictionary làm cơ sở dữ liệu lưu trữ tạm các đối tượng trong bộ nhớ
    cards_database = {}

    while True:
        print("\n====== HỆ THỐNG QUẢN LÝ THẺ THÀNH VIÊN RIKKEI COFFEE ======")
        print("1. Xem danh sách thẻ thành viên")
        print("2. Đăng ký thẻ mới")
        print("3. Khách mua hàng (Tích điểm)")
        print("4. Khách dùng điểm (Đổi ưu đãi)")
        print("5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)")
        print("6. Thoát chương trình")
        print("-----------------------------------------------------------")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        # CHỨC NĂNG 1: XEM DANH SÁCH THẺ THÀNH VIÊN
        if choice == "1":
            print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")
            if not cards_database:
                print("Hệ thống chưa có thẻ thành viên nào.")
            else:
                for c_id, card in cards_database.items():
                    print(f"ID: {card.card_id} | Tên: {card.name:<15} | Điểm: {card.points:<4} | Hạng: {card.tier}")

        # CHỨC NĂNG 2: ĐĂNG KÝ THẺ MỚI
        elif choice == "2":
            print("\n--- ĐĂNG KÝ THẺ MỚI ---")
            card_id = input("Nhập mã số thẻ mới: ").strip().upper()
            
            # Triển khai Static Method để kiểm tra định dạng chuỗi đầu vào đầu tiên
            if not MemberCard.is_valid_card_id(card_id):
                print(" Mã thẻ không đúng định dạng! Vui lòng nhập mẫu chuẩn (Ví dụ: RC01, RC99).")
                continue
                
            if card_id in cards_database:
                print(" Lỗi: Mã thẻ này đã tồn tại trong hệ thống! Vui lòng chọn mã khác.")
                continue
                
            name = input("Nhập tên khách hàng: ").strip()
            if not name:
                print("Tên khách hàng không được để trống!")
                continue

            # Khởi tạo thực thể Object và đưa vào cơ sở dữ liệu lưu trữ
            new_card = MemberCard(card_id, name)
            cards_database[card_id] = new_card
            print("\nĐăng ký thẻ thành viên thành công!")
            print(f"Mã thẻ: {new_card.card_id}\nTên khách hàng: {new_card.name}\nĐiểm ban đầu: {new_card.points}\nHạng thẻ: {new_card.tier}")

        # CHỨC NĂNG 3: KHÁCH MUA HÀNG (TÍCH ĐIỂM)
        elif choice == "3":
            print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")
            card_id = input("Nhập mã số thẻ: ").strip().upper()
            
            if card_id not in cards_database:
                print("Mã số thẻ không tồn tại trên hệ thống!")
                continue
                
            bill = input("Nhập tổng tiền hóa đơn: ").strip()
            cards_database[card_id].earn_points(bill)

        # CHỨC NĂNG 4: KHÁCH DÙNG ĐIỂM (ĐỔI ƯU ĐÃI)
        elif choice == "4":
            print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")
            card_id = input("Nhập mã số thẻ: ").strip().upper()
            
            if card_id not in cards_database:
                print("Mã số thẻ không tồn tại trên hệ thống!")
                continue
                
            print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            pts = input("Nhập số điểm muốn sử dụng: ").strip()
            cards_database[card_id].redeem_points(pts)

        # CHỨC NĂNG 5: CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM
        elif choice == "5":
            print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")
            print(f"Tỷ giá hiện tại là: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            new_val = input("Nhập tỷ giá mới cho 1 điểm: ").strip()
            
            # Kích hoạt Class Method cập nhật đồng bộ toàn bộ lớp dữ liệu
            if MemberCard.update_point_value(new_val):
                print("Cập nhật tỷ giá thành công!")
                print(f"Tỷ giá mới: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")

        # CHỨC NĂNG 6: THOÁT CHƯƠNG TRÌNH
        elif choice == "6":
            print("\nCảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
            break

        # BẪY MENU (Bẫy số 4): Nhập sai dải ký tự số từ 1 đến 6 hoặc nhập chữ bẩn
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()