import logging
from datetime import datetime

# =============================================================================
# 1. CẤU HÌNH MODULE NHẬT KÝ (LOGGING OUT TO TERMINAL)
# =============================================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S,%f'
)

logging.Formatter.formatTime = lambda self, record, datefmt=None: \
    datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]


# =============================================================================
# 2. ĐỊNH NGHĨA NGOẠI LỆ TÙY CHỈNH (CUSTOM EXCEPTIONS)
# =============================================================================
class ItemNotFoundError(Exception):
    """Lỗi quăng ra khi mã đồ uống không tồn tại trong thực đơn."""
    pass


class InvalidQuantityError(Exception):
    """Lỗi quăng ra khi nhân viên nhập số lượng nhỏ hơn hoặc bằng 0."""
    pass


# =============================================================================
# 3. DỮ LIỆU ĐỒNG BỘ CỦA HỆ THỐNG HIGHLANDS
# =============================================================================
DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

current_order = []


# =============================================================================
# 4. ĐỊNH NGHĨA CÁC HÀM XỬ LÝ NGHIỆP VỤ (MODULAR FUNCTIONS)
# =============================================================================

def play_menu():
    """Hiển thị giao diện menu điều khiển chính của Highlands Mini POS."""
    print("\n========== HIGHLANDS MINI POS ==========")
    print("1. Xem thực đơn")
    print("2. Thêm món vào giỏ")
    print("3. Xem giỏ hàng & Tính tổng tiền")
    print("4. Thanh toán & Xóa giỏ hàng")
    print("5. Thoát ca làm việc")
    print("========================================")


# CHỨC NĂNG 1: XEM THỰC ĐƠN
def view_menu():
    """In ra danh sách đồ uống có sẵn trong thực đơn của quán."""
    print("--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, info in DRINK_MENU.items():
        print(f"[{code}] - {info['name']} - {info['price']:,} VNĐ")


def calculate_total(order_list):
    """
    Tính toán tổng tiền hiện có của một giỏ hàng.
    
    Tham số:
        order_list (list): Danh sách các món trong đơn hàng.
    Trả về:
        int: Tổng giá trị tiền của giỏ hàng.
    """
    total = 0
    for item in order_list:
        code = item['code']
        qty = item['quantity']
        price = DRINK_MENU[code]['price']
        total += price * qty
    return total


# CHỨC NĂNG 2: THÊM MÓN VÀO GIỎ
def add_to_order(order_list, drink_code, quantity_str):
    """
    Kiểm tra và thêm món ăn vào giỏ hàng. Quăng lỗi nếu dữ liệu không hợp lệ.
    
    Tham số:
        order_list (list): Giỏ hàng hiện tại cần thêm vào.
        drink_code (str): Mã sản phẩm do nhân viên nhập.
        quantity_str (str): Chuỗi số lượng nhập từ bàn phím.
    """
    code = drink_code.strip().upper()
    
    if code not in DRINK_MENU:
        logging.warning(f"ItemNotFoundError - Code: {code}")
        raise ItemNotFoundError(
            "Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!"
        )
        
    try:
        quantity = int(quantity_str)
    except ValueError:
        logging.error("ValueError - Invalid quantity input")
        raise ValueError("Vui lòng nhập số lượng là một số nguyên!")
        
    if quantity <= 0:
        logging.warning(f"InvalidQuantityError - Quantity: {quantity}")
        raise InvalidQuantityError("Số lượng phải lớn hơn 0!")

    logging.info(f"Added {quantity} of {code} to order")
    
    for item in order_list:
        if item['code'] == code:
            item['quantity'] += quantity
            print(f"Đã cập nhật thêm {quantity} x {DRINK_MENU[code]['name']} vào giỏ hàng.")
            return

    order_list.append({'code': code, 'quantity': quantity})
    print(f"Đã thêm {quantity} x {DRINK_MENU[code]['name']} vào giỏ hàng.")


# CHỨC NĂNG 3: XEM GIỎ HÀNG & TÍNH TỔNG TIỀN
def view_order(order_list):
    """In chi tiết các món ăn có trong giỏ hàng hiện tại và tính tổng tiền."""
    if len(order_list) == 0:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return False 
        
    print("--- GIỎ HÀNG HIỆN TẠI ---")
    print(f"{'Mã SP':<5} | {'Tên đồ uống':<20} | {'Đơn giá':<8} | {'Số lượng':<8} | {'Thành tiền'}")
    print("-" * 64)
    
    for item in order_list:
        code = item['code']
        qty = item['quantity']
        name = DRINK_MENU[code]['name']
        price = DRINK_MENU[code]['price']
        subtotal = price * qty
        print(f"{code:<5} | {name:<20} | {price:Status^,d} | {qty:<8} | {subtotal:,} VNĐ")
        
    print("-" * 64)
    total_money = calculate_total(order_list)
    print(f"Tổng tiền cần thanh toán: {total_money:,} VNĐ")
    return True


# CHỨC NĂNG 4: THANH TOÁN & XÓA GIỎ HÀNG
def checkout(order_list):
    """Thực hiện thanh toán đơn hàng và làm sạch giỏ hàng hiện tại."""
    if len(order_list) == 0:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    print("--- THANH TOÁN ---")
    total_money = calculate_total(order_list)
    print(f"Tổng tiền cần thanh toán: {total_money:,} VNĐ")
    
    confirm = input(f"Xác nhận thanh toán {total_money:,} VNĐ? (y/n): ").strip().lower()
    
    if confirm == 'y':
        print("Thanh toán thành công.")
        logging.info("Checkout successful")
        order_list.clear() 
        print("Giỏ hàng đã được làm trống.")
    elif confirm == 'n':
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")


# =============================================================================
# 5. VÒNG LẶP CHÍNH CHẠY MENU ĐIỀU KHIỂN (MAIN CONSOLE CONTROLLER)
# =============================================================================
def main():
    while True:
        play_menu()
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            view_menu()
        elif choice == "2":
            print("--- THÊM MÓN VÀO GIỎ ---")
            drink_code = input("Nhập mã đồ uống: ")
            quantity_str = input("Nhập số lượng: ")
            try:
                add_to_order(current_order, drink_code, quantity_str)
            except (ItemNotFoundError, InvalidQuantityError, ValueError) as error:
                print(error)
        elif choice == "3":
            view_order(current_order)
        elif choice == "4":
            checkout(current_order)
        elif choice == "5":
            logging.info("Cashier logged out. System shutdown.")
            print("Đã thoát ca làm việc. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main()
