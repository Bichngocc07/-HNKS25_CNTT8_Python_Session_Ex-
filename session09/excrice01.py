# 1. Khởi tạo danh sách kho hàng (Mỗi phần tử là một danh sách con: [Tên, Số lượng])
inventory = [
    ["Iphone 15", 10],
    ["Macbook M3", 5],
    ["Ipad Pro", 8]
]

print("--- HỆ THỐNG QUẢN LÝ KHO HÀNG ---")

# 2. Thêm mới một sản phẩm
new_item_name = input("Nhập tên sản phẩm mới: ").strip()
new_item_qty = int(input("Nhập số lượng: "))
inventory.append([new_item_name, new_item_qty])
print(f"=> Đã thêm {new_item_name} vào kho.")

# 3. Cập nhật số lượng cho sản phẩm đầu tiên (Iphone 15)
# Giả sử nhập thêm 5 chiếc vào kho
add_qty = int(input(f"Nhập số lượng nhập thêm cho {inventory[0][0]}: "))
inventory[0][1] += add_qty 

# 4. Xóa sản phẩm cuối cùng trong danh sách
removed_item = inventory.pop()
print(f"=> Đã xóa sản phẩm cuối cùng: {removed_item[0]}")

# 5. Tính tổng số lượng tất cả sản phẩm còn lại trong kho
total_quantity = 0
print("\n--- BÁO CÁO KHO HÀNG HIỆN TẠI ---")
for item in inventory:
    name = item[0]
    qty = item[1]
    total_quantity += qty
    print(f"- {name}: {qty} chiếc")

print("-" * 30)
print(f"TỔNG SỐ LƯỢNG HÀNG TRONG KHO: {total_quantity} chiếc")