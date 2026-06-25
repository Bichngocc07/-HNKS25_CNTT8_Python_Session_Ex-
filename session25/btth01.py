import re

# =============================================================================
# 1. ĐỊNH NGHĨA LỚP BANKACCOUNT (CORE OOP)
# =============================================================================
class BankAccount:
    # Các thuộc tính cấp lớp (Class Attributes) dùng chung toàn hệ thống
    bank_name = "Vietcombank"
    transaction_fee = 2000  # Mặc định ban đầu phí giao dịch là 2,000 VNĐ

    def __init__(self, account_number, account_name):
        """Hàm khởi tạo một tài khoản Vietcombank mới."""
        # Áp dụng Đóng gói bảo mật (Encapsulation): Chuyển các thuộc tính thành Private (__)
        self.__account_number = account_number
        self.__account_name = None
        self.__balance = 0  # Số dư ban đầu mặc định bằng 0
        
        # Kích hoạt setter để chuẩn hóa tên chủ tài khoản ngay khi khởi tạo
        self.account_name = account_name

    # -------------------------------------------------------------------------
    # CƠ CHẾ ĐÓNG GÓI KIỂM SOÁT DỮ LIỆU (PROPERTY & SETTER)
    # -------------------------------------------------------------------------
    @property
    def account_number(self):
        """Getter cho số tài khoản (Chỉ đọc, không cho sửa)."""
        return self.__account_number

    @property
    def balance(self):
        """Getter cho số dư: Chỉ cấp quyền đọc (Read-only), ngăn chặn sửa đổi lậu."""
        return self.__balance

    @property
    def account_name(self):
        """Getter cho tên chủ tài khoản."""
        return self.__account_name

    @account_name.setter
    def account_name(self, new_name):
        """
        Setter cho account_name (Bẫy lỗi 3): 
        Loại bỏ khoảng trắng thừa, kiểm tra rỗng và tự động viết hoa toàn bộ chuỗi.
        """
        cleaned_name = " ".join(new_name.strip().split())
        
        # Nếu chuỗi rỗng hoặc chỉ chứa khoảng trắng thì bỏ qua và báo lỗi
        if not cleaned_name:
            print("Lỗi: Tên tài khoản không được để trống!")
            return
            
        # Chuẩn hóa viết hoa toàn bộ ký tự (UPPERCASE) theo phom ngân hàng
        self.__account_name = cleaned_name.upper()

    # -------------------------------------------------------------------------
    # PHƯƠNG THỨC TĨNH & PHƯƠNG THỨC LỚP (STATICMETHOD & CLASSMETHOD)
    # -------------------------------------------------------------------------
    @staticmethod
    def validate_account_number(account_number):
        """
        Static Method: Xác thực chuỗi số tài khoản nhập vào.
        Phải là chuỗi số thuần túy (digit) và đạt đúng độ dài 10 ký tự.
        """
        if account_number.isdigit() and len(account_number) == 10:
            return True
        return False

    @classmethod
    def update_transaction_fee(cls, new_fee):
        """Class Method (Chức năng 5): Cập nhật phí rút tiền cho toàn hệ thống."""
        try:
            fee = int(new_fee)
            if fee < 0:
                print("Phí giao dịch không được âm!")
                return False
            cls.transaction_fee = fee
            return True
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")
            return False

    # -------------------------------------------------------------------------
    # CÁC PHƯƠNG THỨC NGHIỆP VỤ ĐỐI TƯỢNG (INSTANCE METHODS)
    # -------------------------------------------------------------------------
    def deposit(self, amount):
        """Nghiệp vụ nạp tiền (Bẫy lỗi 1)."""
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0.")
            return False
            
        self.__balance += amount
        print(f"Nạp tiền thành công: +{amount:,} VNĐ")
        return True

    def withdraw(self, amount):
        """Nghiệp vụ rút tiền (Bẫy lỗi 1 & Bẫy lỗi 2)."""
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0.")
            return False
            
        # Tổng số tiền cần trừ bao gồm số tiền rút + phí rút tiền hệ thống
        total_deduction = amount + BankAccount.transaction_fee
        
        if self.__balance < total_deduction:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch.")
            return False
            
        self.__balance -= total_deduction
        print(f"Rút tiền thành công: -{amount:,} VNĐ")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VNĐ")
        return True

    def display_info(self):
        """Hiển thị chi tiết thông tin tài khoản hiện hành."""
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.__account_number}")
        print(f"Tên chủ tài khoản: {self.__account_name}")
        print(f"Số dư hiện tại: {self.__balance:,} VNĐ")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VNĐ")


# =============================================================================
# 2. VÒNG LẶP ĐIỀU KHIỂN CHƯƠNG TRÌNH CHÍNH (MENU CLI)
# =============================================================================
def main():
    # Biến lưu trữ phiên làm việc của tài khoản hiện tại, ban đầu bằng None
    current_account = None

    while True:
        print("\n====== VIETCOMBANK DIGIBANK SIMULATOR ======")
        print("1. Mở tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Giao dịch Nạp / Rút tiền")
        print("4. Cập nhật tên chủ tài khoản")
        print("5. Đổi phí giao dịch hệ thống (Quản trị viên)")
        print("6. Thoát chương trình")
        print("============================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        # CHỨC NĂNG 1: MỞ TÀI KHOẢN MỚI
        if choice == "1":
            print("\n--- MỞ TÀI KHOẢN MỚI ---")
            acc_num = input("Nhập số tài khoản (đúng 10 chữ số): ").strip()
            
            # Sử dụng Static Method để thẩm định số tài khoản từ chặng đầu
            if not BankAccount.validate_account_number(acc_num):
                print("Số tài khoản không hợp lệ! Phải là chuỗi số có 10 chữ số.")
                continue

            acc_name = input("Nhập tên chủ tài khoản: ").strip()
            if not acc_name:
                print("Tên tài khoản không được để trống!")
                continue

            # Khởi tạo thực thể đối tượng tài khoản mới
            current_account = BankAccount(acc_num, acc_name)
            
            # Kiểm tra trường hợp nếu bộ gán tên bị lỗi rỗng ở bước Setter
            if current_account.account_name is None:
                current_account = None  # Hủy trạng thái khởi tạo
                continue
                
            print("Mở tài khoản thành công!")
            print(f"Số tài khoản: {current_account.account_number}")
            print(f"Tên chủ tài khoản: {current_account.account_name}")

        # BIỆN PHÁP CHẶN TRUY CẬP (Bẫy lỗi 4): Khóa các chức năng 2, 3, 4 nếu chưa tạo tài khoản
        elif choice in ["2", "3", "4"] and current_account is None:
            print("Hệ thống chưa có thông tin tài khoản.")
            print("Vui lòng mở tài khoản ở Chức năng 1 trước.")

        # CHỨC NĂNG 2: XEM THÔNG TIN TÀI KHOẢN
        elif choice == "2":
            print("\n--- THÔNG TIN TÀI KHOẢN ---")
            current_account.display_info()

        # CHỨC NĂNG 3: GIAO DỊCH NẠP / RÚT TIỀN
        elif choice == "3":
            print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
            print("1. Nạp tiền")
            print("2. Rút tiền")
            sub_choice = input("Chọn loại giao dịch (1-2): ").strip()
            
            if sub_choice not in ["1", "2"]:
                print(" Lựa chọn loại giao dịch không hợp lệ.")
                continue
                
            try:
                amount = int(input("Nhập số tiền giao dịch: "))
                
                if sub_choice == "1":
                    if current_account.deposit(amount):
                        print(f"Số dư mới: {current_account.balance:,} VNĐ")
                else:
                    if current_account.withdraw(amount):
                        print(f"Số dư mới: {current_account.balance:,} VNĐ")
                        
            except ValueError:
                print("Lỗi: Vui lòng nhập số tiền là một số nguyên hợp lệ!")

        # CHỨC NĂNG 4: CẬP NHẬT TÊN CHỦ TÀI KHOẢN
        elif choice == "4":
            print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")
            new_name = input("Nhập tên mới: ")
            
            # Lưu lại tên cũ để đối chiếu kiểm tra
            old_name = current_account.account_name
            current_account.account_name = new_name
            
            # Nếu bộ setter từ chối gán (do tên rỗng), giữ nguyên trạng thái cũ
            if current_account.account_name == old_name or current_account.account_name is None:
                print(" Tên tài khoản không được để trống")
                current_account.account_name = old_name  # Khôi phục dữ liệu gốc
            else:
                print(f"Cập nhật thành công. Tên mới: {current_account.account_name}")

        # CHỨC NĂNG 5: ĐỔI PHÍ GIAO DỊCH HỆ THỐNG (ADMIN ONLY)
        elif choice == "5":
            print("\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
            print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VNĐ")
            new_fee = input("Nhập phí giao dịch mới: ").strip()
            
            if BankAccount.update_transaction_fee(new_fee):
                print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {BankAccount.transaction_fee:,} VNĐ")
            else:
                print(f"Phí giao dịch hiện tại vẫn là {BankAccount.transaction_fee:,} VNĐ")

        # CHỨC NĂNG 6: THOÁT CHƯƠNG TRÌNH
        elif choice == "6":
            print("\nCảm ơn bạn đã sử dụng Vietcombank Digibank!")
            break

        # XỬ LÝ LỰA CHỌN MENU SAI QUY ĐỊNH
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()