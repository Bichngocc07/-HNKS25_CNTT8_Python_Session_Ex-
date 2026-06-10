# Biến toàn cục lưu tổng điểm hiện tại của khách hàng
total_points = 100

# ĐÚNG LOGIC: Hàm nhận tham số độc lập và trả về kết quả (Pure Function)
def add_reward_points(current_total, points_earned):
    # Tính toán dựa trên tham số cục bộ truyền vào
    updated_total = current_total + points_earned
    print(f"Đã cộng thêm: {points_earned} điểm.")
    return updated_total  # Trả kết quả về cho bên ngoài sử dụng

# Khách mua hàng được thưởng thêm 50 điểm
# Biến toàn cục hứng lấy giá trị mới được ném ra từ hàm return
total_points = add_reward_points(total_points, 50)

# In ra kết quả kiểm tra
print(f"Tổng điểm hiện tại của khách hàng: {total_points}")