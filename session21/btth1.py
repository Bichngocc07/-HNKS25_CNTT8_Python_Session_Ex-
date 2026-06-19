import logging
import re

# =============================================================================
# CẤU HÌNH NHẬT KÝ GIAO DỊCH (LOGGING)
# =============================================================================
logging.basicConfig(
    filename='momo_transactions.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S,%f',
    level=logging.INFO
)

logging.Formatter.formatTime = lambda self, record, datefmt=None: \
    record.asctime if record.asctime else \
    logging.Formatter().formatTime(record, '%Y-%m-%d %H:%M:%S') + \
    f",{int(record.msecs):03d}"


# =============================================================================
# ĐỊNH NGHĨA CÁC NGOẠI LỆ TÙY CHỈNH
# =============================================================================
class InvalidAmountError(Exception):
    """Lỗi xảy ra khi số tiền giao dịch nhỏ hơn hoặc bằng 0."""
    pass


class InsufficientBalanceError(Exception):
    """Lỗi xảy ra khi số dư không đủ."""
    pass


# Khởi tạo số dư ví ban đầu bằng 0
current_balance = 0


# =============================================================================
# CÁC HÀM CHỨC NĂNG THEO Y HỆT FORM CỦA BẠN
# =============================================================================

def play_menu():
    print("======== VÍ MOMO GIẢ LẬP ========")

    print("1. Nạp tiền vào ví")

    print("2. Chuyển tiền")

    print("3. Xem số dư hiện tại")

    print("4. Thoát chương trình")

    print("================================")


def nap_tien():
    global current_balance
    print("----- NẠP TIỀN VÀO VÍ -----")
    while True:
        try:
            # Sửa tên biến nhập vào thành 'amount' để tránh đè hỏng tên hàm 'nap_tien'
            amount_input = input("Nhập số tiền cần nạp: ").strip()
            amount = int(amount_input)
            
            if amount <= 0:
                logging.error(f"InvalidAmountError: Attempted to process {amount} VND.")
                raise InvalidAmountError("Số tiền giao dịch phải lớn hơn 0.")
                
            current_balance += amount
            print(f"\nNạp tiền thành công: +{amount:,} VND")
            print(f"Số dư hiện tại: {current_balance:,} VND")
                
            # Ghi lại lịch sử giao dịch thành công mức INFO vào file log
            logging.info(f"Deposit successful: +{amount} VND. Current Balance: {current_balance}")
            break
                
        except ValueError:
            logging.error("ValueError: Invalid numeric input for deposit.")
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
            
        except InvalidAmountError as e:
            print(f"Lỗi: {e}")
            break


def chuyen_tien():
    global current_balance
    print("\n----- CHUYỂN TIỀN -----")
    while True:
        phone = input("Nhập số điện thoại người nhận (10 số): ").strip()
        if re.match(r"^\d{10}$", phone):
            break
        print("Lỗi: Số điện thoại phải gồm đúng 10 chữ số.")

    try:
        amount_input = input("Nhập số tiền cần chuyển: ").strip()
        amount = int(amount_input)
        
        if amount <= 0:
            logging.error(f"InvalidAmountError: Attempted to process {amount} VND.")
            raise InvalidAmountError("Số tiền giao dịch phải lớn hơn 0.")
            
        if amount > current_balance:
            logging.error(f"InsufficientBalanceError: Attempted to transfer {amount} VND with balance {current_balance} VND.")
            raise InsufficientBalanceError("Giao dịch thất bại: Số dư của bạn không đủ.")
            
        if amount >= 10000000:
            logging.warning(f"High value transaction detected: {amount} VND to {phone}")
            
        current_balance -= amount
        print(f"\nChuyển tiền thành công tới số điện thoại {phone}.")
        print(f"Số tiền đã chuyển: {amount:,} VND")
        print(f"Số dư còn lại: {current_balance:,} VND")
        
        logging.info(f"Transfer successful: -{amount} VND to {phone}. Current Balance: {current_balance}")
        
    except ValueError:
        print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
    except (InvalidAmountError, InsufficientBalanceError) as e:
        print(f"{e}")
        if isinstance(e, InsufficientBalanceError):
            print(f"Số dư hiện tại: {current_balance:,} VND")


def so_du():
    print("\n----- SỐ DƯ VÍ MOMO -----")
    print(f"Số dư hiện tại: {current_balance:,} VND")
    logging.info(f"Balance checked. Current Balance: {current_balance}")


def main():
    play_menu()
    while True:
        choice = input("Chọn chức năng(1-4): ")
        if choice == "1":
            nap_tien()
        elif choice == "2":
            chuyen_tien()
        elif choice == "3":
            so_du()
        elif choice == "4":
            print("CẢM ƠN BẠN ĐÃ SỬ SỤNG DỊCH VỤ")
            logging.info("System shutdown")
            break
        else:
            print("Lựa chọn không hợp lệ ! Vui lòng chọn từ 1 đến 4 nhé các bạn yêu .")
            play_menu()


# Kích hoạt hệ thống chạy menu điều hướng chính
if __name__ == "__main__":
    main()