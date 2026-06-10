total_points = 100

def add_reward_points(current_total, points_earned):
    updated_total = current_total + points_earned
    print(f"Đã cộng thêm: {points_earned} điểm.")
    return updated_total 


total_points = add_reward_points(total_points, 50)

print(f"Tổng điểm hiện tại của khách hàng: {total_points}")
