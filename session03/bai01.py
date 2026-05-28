print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")

# ĐÚNG LOGIC: Khởi tạo "chiếc hộp" đựng tổng tiền Ở NGOÀI vòng lặp
# Điều này giúp chiếc hộp không bị làm trống lại mỗi khi có nhân viên mới
total_budget = 0

# Vòng lặp chạy 3 lần để nhập lương cho 3 nhân viên (từ 1 đến 3)
for employee_number in range(1, 4):
    print(f"\nĐang xử lý nhân viên số: {employee_number}")
    
    # Nhập mức lương và ép kiểu sang số nguyên
    salary = int(input("Nhập mức lương (VND): "))
    
    # Thực hiện thao tác cộng dồn thêm tiền vào chiếc hộp tổng
    total_budget = total_budget + salary

print("\n" + "="*50)
# Sau khi nhập xong toàn bộ nhân viên, in tổng tiền ra màn hình
print(f"==> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ: {total_budget} VND")
print("="*50)