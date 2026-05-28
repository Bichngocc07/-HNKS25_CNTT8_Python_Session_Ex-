print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")

while True:
    employee_quantity = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))

    if employee_quantity <= 0:
        print("[LỖI] Số lượng không hợp lệ: Vui lòng nhập một con số lớn hơn 0.\n")
        
    else:
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {employee_quantity} nhân sự mới!")
        
        break

print("======= CHƯƠNG TRÌNH KẾT THÚC =======")
