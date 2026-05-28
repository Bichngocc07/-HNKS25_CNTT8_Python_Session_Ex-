print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

# Vòng lặp chạy đúng 3 lần cho 3 nhân viên
for employee_number in range(1, 4):
    print(f"\n--- Đang xử lý nhân viên số: {employee_number} ---")
    
    # Kế toán nhập số ngày công
    working_days = int(input("Nhập số ngày công trong tháng: "))
    
    # Kiểm tra điều kiện ngày công bằng 0
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        print("======================================")
        # CHỐT CHẶN: Bỏ qua các lệnh phía dưới, chuyển ngay sang nhân viên tiếp theo
        continue
        
    # Luồng xử lý tính thưởng và gửi email (Chỉ chạy khi working_days > 0)
    bonus_amount = working_days * 200000
    print(f"-> Đã gửi Email: Chúc mừng nhận được {bonus_amount} VND tiền thưởng!")
    print("======================================")

print("\nĐã hoàn tất quá trình duyệt thưởng cho 3 nhân viên.")