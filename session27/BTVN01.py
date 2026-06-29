import os
from abc import ABC, abstractmethod

# =============================================================================
# 1. LỚP CHA TRỪU TƯỢNG VÀ CÁC LỚP BỔ TRỢ TIỆN ÍCH
# =============================================================================

class BaseAccount(ABC):
    """
    Abstract Base Class (ABC) định nghĩa bộ khung chuẩn cho mọi tài khoản.
    Sử dụng abc.ABC để bắt buộc tính trừu tượng, ngăn chặn khởi tạo trực tiếp (Bẫy 1).
    """
    bank_name = "Vietcombank"

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.__account_name = None
        self._balance = 0.0  # Đóng gói số dư thuộc tính bảo mật nội bộ
        
        # Kích hoạt setter chuẩn hóa tên chủ tài khoản ngay khi khởi tạo
        self.account_name = account_name

    @property
    def account_name(self):
        """Property giải bọc lấy thông tin tên chủ tài khoản."""
        return self.__account_name

    @account_name.setter
    def account_name(self, name):
        """Setter tự động xóa khoảng trắng thừa và ép kiểu chữ IN HOA."""
        self.__account_name = " ".join(name.strip().split()).upper()

    @property
    def balance(self):
        """Property cấp quyền chỉ đọc (Read-only) số dư, bảo vệ dòng tiền."""
        return self._balance

    @abstractmethod
    def deposit(self, amount):
        """Phương thức trừu tượng bắt buộc các lớp con phải ghi đè logic nạp tiền."""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Phương thức trừu tượng bắt buộc các lớp con phải ghi đè logic rút tiền."""
        pass

    # -------------------------------------------------------------------------
    # NẠP CHỒNG TOÁN TỬ (OPERATOR OVERLOADING)
    # -------------------------------------------------------------------------
    def __add__(self, other):
        """Nạp chồng toán tử '+': Cộng gộp số dư của hai đối tượng tài khoản (Bẫy 3)."""
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance + other.balance

    def __lt__(self, other):
        """Toán tử '<' (Less Than): So sánh số dư giữa hai tài khoản hệ thống (Bẫy 3)."""
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance < other.balance

    # -------------------------------------------------------------------------
    # STATIC METHOD & CLASS METHOD
    # -------------------------------------------------------------------------
    @staticmethod
    def validate_account_number(account_number):
        """Static Method: Hàm tiện ích độc lập dùng để thẩm định số tài khoản đúng 10 chữ số."""
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_bank_name(cls, new_name):
        """Class Method: Nhận tham số lớp (cls) để cập nhật tên ngân hàng toàn hệ thống."""
        cls.bank_name = new_name


class DigitalPremiumMixin:
    """Lớp độc lập độc quyền cung cấp tính năng hoàn tiền cao cấp cho dịch vụ số."""
    def cashback_reward(self, account, amount):
        """Hoàn tiền 1% cho các giao dịch trực tuyến lớn hơn 5,000,000 VND."""
        if amount > 5000000:
            reward = amount * 0.01
            account._balance += reward
            print(f"\n[Ưu đãi Premium]: Bạn được hoàn tiền 1% ({reward:,} VND) vào tài khoản!")
            return reward
        return 0


# =============================================================================
# 2. ĐỊNH NGHĨA CÁC PHÂN HỆ TÀI KHOẢN CON (SUBCLASSES)
# =============================================================================

class SavingsAccount(BaseAccount):
    """Phân hệ tài khoản phục vụ khách hàng gửi tiết kiệm sinh lãi."""
    def __init__(self, account_number, account_name, interest_rate):
        # Kế thừa thuộc tính cơ bản của lớp cha thông qua super()
        super().__init__(account_number, account_name)
        self.interest_rate = float(interest_rate)

    def deposit(self, amount):
        """Ghi đè phương thức: Nạp tiền tăng số dư bình thường."""
        if amount <= 0:
            print("Số tiền nạp phải lớn hơn 0 VND.")
            return False
        self._balance += amount
        return True

    def withdraw(self, amount):
        """Ghi đè phương thức: Phạt 2% trên số tiền rút nếu rút trước hạn."""
        if amount <= 0:
            print("Số tiền rút phải lớn hơn 0 VND.")
            return False
        
        penalty_fee = amount * 0.02
        total_deduction = amount + penalty_fee
        
        if self._balance < total_deduction:
            print("❌ Giao dịch thất bại: Số dư tài khoản không đủ thanh toán tiền rút và phí phạt.")
            return False
            
        self._balance -= total_deduction
        print(f"Số tiền rút: {amount:,} VND")
        print(f"Phí phạt rút trước hạn (2%): {penalty_fee:,} VND")
        return True

    def apply_interest(self):
        """Tính toán tiền lãi dựa trên số dư hiện tại và cộng trực tiếp vào tài khoản."""
        interest_earned = self.balance * self.interest_rate
        self._balance += interest_earned
        return interest_earned


class CreditAccount(BaseAccount):
    """Phân hệ tài khoản tiêu trước trả sau, cho phép thấu chi âm tiền."""
    def __init__(self, account_number, account_name, credit_limit=20000000.0):
        super().__init__(account_number, account_name)
        self.credit_limit = float(credit_limit)

    def deposit(self, amount):
        """Ghi đè phương thức: Logic trả nợ thấu chi (Tăng số dư/giảm nợ)."""
        if amount <= 0:
            print("Số tiền nạp phải lớn hơn 0 VND.")
            return False
        self._balance += amount
        return True

    def withdraw(self, amount):
        """Ghi đè phương thức (Bẫy 2): Cho phép số dư âm trong hạn mức cho phép."""
        if amount <= 0:
            print("Số tiền rút phải lớn hơn 0 VND.")
            return False
            
        # Kiểm tra điều kiện thấu chi an toàn
        if self._balance - amount < -self.credit_limit:
            print("❌ Giao dịch thất bại: Vượt quá hạn mức thấu chi cho phép!")
            return False
            
        self._balance -= amount
        print(f"Số tiền rút: {amount:,} VND (Sử dụng hạn mức thấu chi)")
        return True


class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    """
    Tài khoản đa năng thế hệ mới, đa kế thừa từ SavingsAccount và DigitalPremiumMixin.
    Đảm bảo quy tắc MRO hoạt động chuẩn xác theo sơ đồ hình thoi.
    """
    def __init__(self, account_number, account_name, interest_rate):
        # Thiết lập cấu trúc phân cấp tuần tự qua super() tương ứng với MRO danh sách
        super().__init__(account_number, account_name, interest_rate)


# =============================================================================
# 3. PHÂN HỆ CỔNG THANH TOÁN INTERFACE (DUCK TYPING CORES)
# =============================================================================

class VNPayGateway:
    """Cổng thanh toán độc lập VNPay."""
    def execute_pay(self, account, amount):
        print(f"[Hệ thống VNPay]: Đang kết nối tới tài khoản {account.account_number}...")
        return True


class ViettelMoneyGateway:
    """Cổng thanh toán độc lập Viettel Money."""
    def execute_pay(self, account, amount):
        print(f"[Hệ thống Viettel Money]: Đang xử lý giao dịch an toàn...")
        return True


# Hàm toàn cục độc lập áp dụng cơ chế Duck Typing (Bẫy 4)
def process_payment(payment_gateway, account, amount):
    """
    Hàm xử lý thanh toán hóa đơn không quan tâm gateway thuộc class nào,
    miễn là đối tượng đó có phương thức 'execute_pay'.
    """
    try:
        # Kiểm tra hành vi xem đối tượng truyền vào có hàm execute_pay hay không
        if not hasattr(payment_gateway, "execute_pay"):
            raise AttributeError("Cổng thanh toán không hợp lệ hoặc chưa được tích hợp")
            
        if account.balance < amount and not isinstance(account, CreditAccount):
            print("❌ Thanh toán thất bại: Số dư tài khoản không đủ để thực hiện hóa đơn.")
            return False
            
        # Kích hoạt cổng thực thi thanh toán độc lập
        gateway_status = payment_gateway.execute_pay(account, amount)
        if gateway_status:
            # Khấu trừ dòng tiền của tài khoản qua phương thức rút tiền
            account._balance -= amount
            print("Xác thực thanh toán bằng Duck Typing thành công!")
            print(f"Tài khoản đã thanh toán hóa đơn giá trị: {amount:,} VND.")
            print(f"Số dư mới: {account.balance:,} VND.")
            
            # Nếu tài khoản hiện hành là tài khoản Hybrid, kích hoạt thêm hoàn tiền Mixin số
            if isinstance(account, HybridAccount):
                account.cashback_reward(account, amount)
            return True
            
    except AttributeError as e:
        print(f"❌ [LỖI HỆ THỐNG]: {e}")
        return False


# =============================================================================
# 4. GIAO DIỆN HỆ THỐNG MENU ĐIỀU HÀNH CHÍNH (CLI MAIN CONTROLLER)
# =============================================================================

def main():
    accounts = []
    current_account = None

    while True:
        print("\n===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====")
        print("1. Mở tài khoản mới (Chọn loại tài khoản)")
        print("2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)")
        print("3. Giao dịch Nạp / Rút tiền & Tính điểm thưởng (Đa hình)")
        print("4. Tích lũy / Áp dụng lãi suất định kỳ")
        print("5. Kiểm tra tính năng gộp tài khoản & So sánh (Overloading)")
        print("6. Thanh toán hóa đơn qua Cổng trung gian (Duck Typing)")
        print("7. Thoát chương trình")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-7): ").strip()

        # CHỨC NĂNG 1: MỞ TÀI KHOẢN MỚI
        if choice == "1":
            print("\n--- CHỌN LOẠI TÀI KHOẢN ---")
            print("1. Savings Account (Tài khoản Tiết kiệm)")
            print("2. Credit Account (Tài khoản Tín dụng)")
            print("3. Hybrid Account (Tài khoản Đa năng)")
            type_choice = input("Chọn loại tài khoản (1-3): ").strip()
            
            if type_choice not in ["1", "2", "3"]:
                print("Lựa chọn không hợp lệ!")
                continue
                
            acc_num = input("Nhập số tài khoản 10 chữ số: ").strip()
            # Sử dụng Static Method thẩm định số tài khoản đầu vào
            if not BaseAccount.validate_account_number(acc_num):
                print("Số tài khoản không hợp lệ! Phải gồm đúng 10 chữ số.")
                continue
                
            name = input("Nhập tên chủ tài khoản: ")
            
            if type_choice == "1":
                rate = input("Nhập lãi suất năm (ví dụ 0.06): ").strip()
                current_account = SavingsAccount(acc_num, name, rate)
                print("\nMở tài khoản Tiết kiệm thành công!")
            elif type_choice == "2":
                limit = input("Nhập hạn mức tín dụng (Ấn Enter để chọn mặc định 20M): ").strip()
                if limit == "":
                    current_account = CreditAccount(acc_num, name)
                else:
                    current_account = CreditAccount(acc_num, name, float(limit))
                print("\nMở tài khoản Tín dụng thành công!")
            elif type_choice == "3":
                rate = input("Nhập lãi suất năm (ví dụ 0.06): ").strip()
                current_account = HybridAccount(acc_num, name, rate)
                print("\nMở tài khoản Đa năng Hybrid thành công!")
                
            accounts.append(current_account)
            print(f"Chủ tài khoản: {current_account.account_name}")

        # BIỆN PHÁP KHÓA AN TOÀN TRUY CẬP (Bẫy số 4): Yêu cầu tài khoản active trước
        elif choice in ["2", "3", "4", "5", "6"] and current_account is None:
            print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản ở Chức năng 1 trước.")

        # CHỨC NĂNG 2: XEM THÔNG TIN VÀ KIỂM TRA MRO
        elif choice == "2":
            print("\n--- THÔNG TIN TÀI KHOẢN HIỆN TẠI ---")
            print(f"Loại tài khoản: {type(current_account).__name__}")
            print(f"Ngân hàng: {current_account.bank_name}")
            print(f"Số tài khoản: {current_account.account_number}")
            print(f"Chủ tài khoản: {current_account.account_name}")
            print(f"Số dư: {current_account.balance:,} VND")
            
            if hasattr(current_account, "interest_rate"):
                print(f"Lãi suất: {current_account.interest_rate * 100}% / năm")
            if isinstance(current_account, CreditAccount):
                print(f"Hạn mức tín dụng: {current_account.credit_limit:,} VND")
                
            print("\n[Kiểm tra kỹ thuật MRO kế thừa]:")
            for idx, cls in enumerate(type(current_account).__mro__, 1):
                print(f"  {idx}. {cls}")

        # CHỨC NĂNG 3: GIAO DỊCH NẠP / RÚT TIỀN (ĐA HÌNH)
        elif choice == "3":
            print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
            print("1. Nạp tiền")
            print("2. Rút tiền")
            tx_choice = input("Chọn giao dịch (1-2): ").strip()
            
            try:
                amount = float(input("Nhập số tiền giao dịch: ").replace(",", ""))
                if tx_choice == "1":
                    if current_account.deposit(amount):
                        # Khởi chạy logic hoàn tiền Mixin độc quyền cho tài khoản Hybrid khi nạp giao dịch số
                        if isinstance(current_account, HybridAccount):
                            current_account.cashback_reward(current_account, amount)
                        print(f"Nạp tiền thành công! Số dư mới: {current_account.balance:,} VND")
                elif tx_choice == "2":
                    current_account.withdraw(amount)
            except ValueError:
                print("Vui lòng nhập định dạng số tiền hợp lệ!")

        # CHỨC NĂNG 4: ÁP DỤNG LÃI SUẤT ĐỊNH KỲ
        elif choice == "4":
            print("\n--- TÍNH LÃI ĐỊNH KỲ ---")
            if hasattr(current_account, "apply_interest"):
                old_bal = current_account.balance
                interest = current_account.apply_interest()
                print(f"Số dư trước tính lãi: {old_bal:,} VND")
                print(f"Lãi suất năm: {current_account.interest_rate * 100}%")
                print(f"Tiền lãi nhận được: +{interest:,} VND")
                print(f"Số dư mới sau khi cộng lãi: {current_account.balance:,} VND")
            else:
                print("❌ Tính năng không hỗ trợ cho loại tài khoản hiện tại (Tín dụng không sinh lãi).")

        # CHỨC NĂNG 5: GỘP VÀ SO SÁNH TÀI KHOẢN (OPERATOR OVERLOADING)
        elif choice == "5":
            print("\n--- ĐỒNG BỘ & SO SÁNH TÀI KHOẢN (OPERATOR OVERLOADING) ---")
            print(f"Tài khoản hiện tại (A): {current_account.account_name} (Số dư: {current_account.balance:,} VND)")
            
            opp_num = input("Chọn tài khoản đối ứng (B) từ danh sách hệ thống bằng cách nhập STK: ").strip()
            opp_account = None
            for acc in accounts:
                if acc.account_number == opp_num:
                    opp_account = acc
                    break
                    
            if opp_account is None:
                print("❌ Không tìm thấy tài khoản đối ứng hợp lệ trong hệ thống database!")
                continue
                
            # Kiểm tra toán tử so sánh __lt__ gán nhãn Overloading
            if current_account < opp_account:
                compare_res = "Số dư tài khoản A NHỎ HƠN số dư tài khoản B."
            else:
                compare_res = "Số dư tài khoản A LỚN HƠN HOẶC BẰNG số dư tài khoản B."
                
            # Kiểm tra toán tử cộng gộp __add__ gán nhãn Overloading
            total_sum = current_account + opp_account
            
            print(f"[Kết quả So sánh (__lt__)]: {compare_res}")
            print(f"[Kết quả Tổng hợp (__add__)]: Tổng số tiền sở hữu của cả 2 tài khoản là: {total_sum:,} VND.")

        # CHỨC NĂNG 6: THANH TOÁN HÓA ĐƠN QUA CỔNG TRUNG GIAN (DUCK TYPING)
        elif choice == "6":
            print("\n--- THANH TOÁN HÓA ĐƠN QUA CỔNG TRUNG GIAN ---")
            print("1. Thanh toán qua VNPay")
            print("2. Thanh toán qua Viettel Money")
            print("3. Thử nghiệm truyền cổng lỗi phá hoại (Bẫy 4)")
            gateway_choice = input("Chọn cổng thanh toán (1-3): ").strip()
            
            if gateway_choice == "1":
                gateway = VNPayGateway()
            elif gateway_choice == "2":
                gateway = ViettelMoneyGateway()
            elif gateway_choice == "3":
                gateway = "Một Chuỗi Ký Tự Phá Hoại Hệ Thống"  # Không có hàm execute_pay
            else:
                print("Lựa chọn không hợp lệ!")
                continue
                
            try:
                bill_amount = float(input("Nhập số tiền hóa đơn: "))
                process_payment(gateway, current_account, bill_amount)
            except ValueError:
                print("Vui lòng nhập số tiền hóa đơn hợp lệ.")

        # CHỨC NĂNG 7: THOÁT CHƯƠNG TRÌNH
        elif choice == "7":
            print("\nCảm ơn đã trải nghiệm hệ thống Vietcombank Digibank Pro Simulator!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1 đến 7.")


if __name__ == "__main__":
    # Thử nghiệm Bẫy số 1 bảo vệ lớp trừu tượng trước khi vào vòng lặp chính
    try:
        print("[Kiểm tra hệ thống độc lập]: Thử khởi tạo trực tiếp BaseAccount...")
        acc = BaseAccount("0000000000", "Lỗi")
    except TypeError:
        print("🛡️ [BẢO VỆ]: Chặn đứng thành công hành vi khởi tạo lớp trừu tượng BaseAccount trực tiếp!")
        
    main()