def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total  

order_total = calculate_final_price(100000, 0.1, 15000)

final_payment = order_total + 5000

print(f"Khách hàng cần thanh toán: {int(final_payment)}.0")
