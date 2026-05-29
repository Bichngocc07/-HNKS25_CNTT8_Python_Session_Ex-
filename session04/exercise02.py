# Chức năng 1: Sử dụng vòng lặp chạy đúng 7 lần để yêu cầu người dùng nhập vào doanh thu của từng ngày (In rõ thông báo từ "Ngày 1" đến "Ngày 7").
# Chức năng 2: Sử dụng các biến tích lũy để tính toán:
# Tổng doanh thu của cả tuần.
# Doanh thu trung bình mỗi ngày trong tuần.
# Chức năng 3: Đếm xem có bao nhiêu ngày có doanh thu đạt từ 5,000,000 VND trở lên.
# Input
# Doanh thu của từng ngày (7 ngày) - Dùng vòng lặp for
# Output
# Tổng doanh thu của cả tuần = Doanh thu ngày 1 + Doanh thu ngày 2 + ... + Doanh thu ngày 7
# Doanh thu trung bình mỗi ngày = Tổng doanh thu của cả tuần / 7
# Số ngày có doanh thu đạt từ 5,000,000 VND trở lên(tạo biến đếm , kiểm tra điều kiện và tăng biến đếm lên 1 đơn vị)
total_revenue = 0
count = 0
for i in range(1, 8):
    revenue = int(input(f"Nhập doanh thu của ngày {i}: "))
    total_revenue = total_revenue + revenue
    if revenue >= 5000000:
        count += 1
print("Tổng doanh thu của cả tuần: ", total_revenue)
print("Doanh thu trung bình mỗi ngày: ", total_revenue / 7)
print("Số ngày có doanh thu đạt từ 5,000,000 VND trở lên: ", count)