print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")

# Áp dụng Giải pháp 1: Tạo vòng lặp vô hạn để ép người dùng nhập đúng
while True:
    # Bọc khối try-except để xử lý bẫy nếu chuyên viên HR gõ nhầm ký tự chữ (Ví dụ: "năm")
    try:
        employee_quantity = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
    except ValueError:
        print("[LỖI] Dữ liệu nhập vào phải là một số nguyên cụ thể.\n")
        continue # Ép vòng lặp quay lại từ đầu để nhập lại

    # Xử lý Edge Cases: Bẫy nhập số 0 và bẫy nhập số âm
    if employee_quantity <= 0:
        print("[LỖI] Số lượng không hợp lệ: Vui lòng nhập một con số lớn hơn 0.\n")
        # Không có lệnh break, vòng lặp tự động quay lại yêu cầu nhập tiếp
    else:
        # Dữ liệu hoàn toàn hợp lệ (> 0)
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {employee_quantity} nhân sự mới!")
        # CHỐT CHẶN: Bẻ gãy vòng lặp để chuyển sang phần tiếp theo của chương trình
        break

print("======= CHƯƠNG TRÌNH KẾT THÚC =======")