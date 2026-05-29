# Chức năng 1: Yêu cầu người dùng nhập vào tổng số lượng hóa đơn đã xuất trong ca .
# Chức năng 2: Lặp và nhập giá trị cho từng hóa đơn.
# Chức năng 3: Tìm ra giá trị hóa đơn lớn nhất (Max) và nhỏ nhất (Min) sau khi kết thúc việc nhập.
# Input
# Tổng số lượng hóa đơn đã xuất trong ca (số nguyên).
# Giá trị của từng hóa đơn (số nguyên) - Dùng vòng lặp for
# Output
# Giá trị hóa đơn lớn nhất (Max) và nhỏ nhất (Min) sau khi kết thúc việc nhập.
sum = 0
max = 0
min = 0
quantity = int(input("Nhập tổng số lượng hóa đơn đã xuất trong ca: "))
for i in range(1, quantity + 1):
    price = int(input(f"Nhập giá trị của hóa đơn {i}: "))
    # price là giá trị từng đơn
    if price > max:
        max = price # = là toán tử gán, sẽ truyền giá trị price vào max 
    # nếu giá trị price lớn hơn max hiện tại thì truyền giá trị đó vào max
    if price < min or min == 0:
        min = price


print("Giá trị hóa đơn lớn nhất (Max): ", max)
print("Giá trị hóa đơn nhỏ nhất (Min): ", min)