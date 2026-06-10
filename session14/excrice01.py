# ĐÚNG LOGIC: Hàm tính tổng tiền hóa đơn mua hàng sử dụng lệnh return để trả kết quả về
def calculate_final_price(price, discount, shipping_fee):
    # Công thức tính: Tổng tiền = Giá gốc - (Giá gốc * Tỉ lệ giảm) + Phí ship
    total = price - (price * discount) + shipping_fee
    return total  # Bắt buộc phải có return để biến bên ngoài hứng được dữ liệu

# ĐÚNG THỨ TỰ: Truyền tham số đúng vị trí (Giá gốc, Tỉ lệ giảm 10%, Phí ship 15k)
order_total = calculate_final_price(100000, 0.1, 15000)

# Hệ thống cộng thêm 5,000 VNĐ phí đóng gói vào tổng tiền hàng
final_payment = order_total + 5000

# ĐÚNG YÊU CẦU: Console in ra đúng 1 dòng duy nhất (Định dạng số nguyên)
print(f"Khách hàng cần thanh toán: {int(final_payment)}.0")