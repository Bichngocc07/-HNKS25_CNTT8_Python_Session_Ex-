# 1. Danh sách ban đầu gồm các đơn hàng cần xử lý
express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

# 2. Thêm đơn hàng mới "GE104" vào cuối mảng
express_orders.append("GE104")

# 3. Chèn đơn hàng hỏa tốc "GE100-FAST" lên đầu mảng (Index 0)
express_orders.insert(0, "GE100-FAST")
# Lúc này danh sách là: ["GE100-FAST", "GE101", "GE102-WRONG", "GE103-CANCEL", "GE104"]

# 4. Sửa mã đơn hàng lỗi ở vị trí index 2 thành mã đúng
express_orders[2] = "GE102-UPDATED"

# 5. Xóa đơn hàng bị hủy theo giá trị chữ cụ thể
express_orders.remove("GE103-CANCEL")

# 6. Lấy đơn hàng đầu tiên (Index 0) ra để đi giao và lưu vào biến
current_order = express_orders.pop(0)

# 7. In kết quả kiểm tra hệ thống điều phối điều phối
print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)