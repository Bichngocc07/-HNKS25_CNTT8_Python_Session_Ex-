import re

# =============================================================================
# 1. ĐỊNH NGHĨA LỚP NETFLIXACCOUNT (CORE OOP)
# =============================================================================
class NetflixAccount:
    platform_name = "Netflix"
    max_profiles = 5  

    def __init__(self, email, password):
        """Hàm khởi tạo tài khoản Netflix mới."""
        self.email = email
        
        self.__password = None
        self.__plan = "Basic"  
        self.profiles = []    
        
        self.password = password

    # -------------------------------------------------------------------------
    # CƠ CHẾ ĐÓNG GÓI BẢO MẬT (PROPERTY & SETTER)
    # -------------------------------------------------------------------------
    @property
    def password(self):
        """Getter cho password: Chỉ trả về chuỗi ký tự ẩn danh bảo mật."""
        return "********"

    @password.setter
    def password(self, new_password):
        """
        Setter cho password (Bẫy lỗi 2): 
        Kiểm tra độ dài mật khẩu phải từ 5 ký tự trở lên.
        """
        if len(new_password) < 5:
            raise ValueError("Password is too short")
        self._NetflixAccount__password = new_password  # Gán an toàn qua mangling

    @property
    def plan(self):
        """Getter cho plan: Chỉ cấp quyền đọc (Read-only), không có Setter."""
        return self.__plan

    # -------------------------------------------------------------------------
    # PHƯƠNG THỨC TĨNH & PHƯƠNG THỨC LỚP (STATICMETHOD & CLASSMETHOD)
    # -------------------------------------------------------------------------
    @staticmethod
    def validate_email(email):
        """
        Static Method (Bẫy lỗi 1): Kiểm tra chuỗi email truyền vào.
        Phải chứa ký tự '@' và không được để trống.
        """
        if "@" in email and len(email.strip()) > 0:
            return True
        return False

    @classmethod
    def update_max_profiles(cls, new_limit):
        """Class Method (Chức năng 5): Cập nhật giới hạn hồ sơ toàn hệ thống."""
        try:
            limit = int(new_limit)
            if limit > 0:
                cls.max_profiles = limit
                return True
            print("Số lượng giới hạn Profile phải lớn hơn 0!")
            return False
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")
            return False

    # -------------------------------------------------------------------------
    # PHƯƠNG THỨC NGHIỆP VỤ ĐỐI TƯỢNG (INSTANCE METHODS)
    # -------------------------------------------------------------------------
    def add_profile(self, profile_name):
        """Chức năng 3 (Bẫy lỗi 3): Thêm tên người xem mới vào danh sách."""
        name = profile_name.strip()
        if not name:
            print("Tên người xem không được để trống!")
            return

        if len(self.profiles) >= NetflixAccount.max_profiles:
            print(f"Đã đạt giới hạn số lượng Profile trên tài khoản này ({NetflixAccount.max_profiles} độc quyền)!")
            return

        self.profiles.append(name)
        print(f"Đã thêm thành công người xem: '{name}'")

    def upgrade_plan(self, new_plan):
        """Chức năng 4: Nâng cấp gói cước sử dụng."""
        valid_plans = ["Basic", "Standard", "Premium"]
        if new_plan in valid_plans:
            self.__plan = new_plan
            print(f"Nâng cấp gói cước thành công! Gói hiện tại của bạn: {self.__plan}")
            return True
        else:
            print(f"Gói cước không hợp lệ! Chỉ chấp nhận: {', '.join(valid_plans)}")
            return False

    def display_info(self):
        """Chức năng 2: Hiển thị toàn bộ thông tin chi tiết tài khoản."""
        print(f" Nền tảng: {NetflixAccount.platform_name}")
        print(f" Email tài khoản: {self.email}")
        print(f" Mật khẩu: {self.password}")  # Gọi qua property sẽ ra "********"
        print(f" Gói dịch vụ: {self.__plan}")
        print(f" Danh sách Profile người xem ({len(self.profiles)}/{NetflixAccount.max_profiles}):")
        if not self.profiles:
            print("   (Chưa có hồ sơ người xem nào)")
        else:
            for p in self.profiles:
                print(f"   [-] {p}")


# =============================================================================
# 2. VÒNG LẶP ĐIỀU KHIỂN CHƯƠNG TRÌNH CHÍNH (MENU)
# =============================================================================
def main():
    current_account = None

    while True:
        print("\n****** NETFLIX ACCOUNT MANAGER ******")
        print("1. Đăng ký tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Thêm người xem")
        print("4. Nâng cấp gói cước")
        print("5. Cập nhật chính sách Netflix (Admin Only)")
        print("6. Thoát chương trình")
        print("*************************************")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        # CHỨC NĂNG 1: ĐĂNG KÝ TÀI KHOẢN MỚI
        if choice == "1":
            print("\n--- ĐĂNG KÝ TÀI KHOẢN ---")
            email = input("Nhập Email đăng ký: ").strip()
            
            if not NetflixAccount.validate_email(email):
                print(" Email không hợp lệ, vui lòng chứa ký tự '@'!")
                continue

            password = input("Nhập Mật khẩu (tối thiểu 5 ký tự): ")
            
            try:
                current_account = NetflixAccount(email, password)
                print("Đăng ký tài khoản mới và đăng nhập thành công!")
            except ValueError as e:
                print(f" Đăng ký thất bại! Lỗi bảo mật: {e}. Vui lòng thử lại.")
                current_account = None

        # CHỨC NĂNG CHẶN TRUY CẬP (Bẫy lỗi 4): Nếu chưa đăng nhập, khóa chức năng 2, 3, 4
        elif choice in ["2", "3", "4"] and current_account is None:
            print("⚠️ Cảnh báo: Vui lòng đăng nhập hoặc đăng ký tài khoản trước (Chức năng 1)!")

        # CHỨC NĂNG 2: XEM THÔNG TIN TÀI KHOẢN
        elif choice == "2":
            print("\n--- THÔNG TIN TÀI KHOẢN NETFLIX ---")
            current_account.display_info()

        # CHỨC NĂNG 3: THÊM NGƯỜI XEM (PROFILE)
        elif choice == "3":
            print("\n--- THÊM NGƯỜI XEM MỚI ---")
            profile_name = input("Nhập tên người xem mới (Ví dụ: Bố Mẹ, Con Gái): ")
            current_account.add_profile(profile_name)

        # CHỨC NĂNG 4: NÂN CẤP GÓI CƯỚC
        elif choice == "4":
            print("\n--- NÂN CẤP GÓI CƯỚC DỊCH VỤ ---")
            print("Các gói hiện có: Basic, Standard, Premium")
            new_plan = input("Nhập tên gói muốn nâng cấp: ").strip()
            current_account.upgrade_plan(new_plan)

        # CHỨC NĂNG 5: CẬP NHẬT CHÍNH SÁCH NETFLIX (ADMIN ONLY)
        elif choice == "5":
            print("\n--- CẬP NHẬT CHÍNH SÁCH HỆ THỐNG (ADMIN ONLY) ---")
            print(f"Giới hạn Profile toàn cầu hiện tại: {NetflixAccount.max_profiles}")
            new_limit = input("Nhập số lượng giới hạn Profile tối đa mới: ").strip()
            
            if NetflixAccount.update_max_profiles(new_limit):
                print(f"Đã cập nhật giới hạn Profile toàn hệ thống thành: {NetflixAccount.max_profiles}")

        # CHỨC NĂNG 6: THOÁT CHƯƠNG TRÌNH
        elif choice == "6":
            print("\nCảm ơn quý khách đã sử dụng hệ thống tài khoản Netflix! Tạm biệt.")
            break

        # BẪY MENU KHÔNG HỢP LỆ
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn số từ 1 đến 6.")


if __name__ == "__main__":
    main()
