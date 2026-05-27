print("     MODULE KHỞI TẠO & PHÂN LUỒNG BỆNH ÁN SỐ")

# 1. Tiếp nhận dữ liệu đầu vào
name_input = input("Nhập họ và tên bệnh nhân: ")
# Loại bỏ khoảng trắng thừa ở hai đầu chuỗi để chống bẫy chỉ nhập dấu cách (space)
patient_name = name_input.strip()

# Bọc trong khối try-except phòng trường hợp lễ tân nhập chữ vào ô tuổi gây crash
try:
    patient_age = int(input("Nhập tuổi bệnh nhân: "))
except ValueError:
    # Kích hoạt nếu nhập tuổi là ký tự chữ (ví dụ: "hai mươi")
    patient_age = -1 

print("\n" + "-"*50)

# 2. Chốt chặn Gateway: Kiểm tra và xử lý triệt để các bẫy dữ liệu (Edge Cases)
if patient_name == "" or patient_age < 0 or patient_age > 150:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    print("Hệ thống đã chặn dữ liệu rác. Tiến trình phân luồng bị hủy.")
    print("-" * 50)
else:
    # 3. Phân luồng nghiệp vụ tự động (Khi dữ liệu đã hợp lệ hoàn toàn)
    if patient_age < 6:
        classification = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
    elif patient_age >= 80:
        classification = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
    else:
        classification = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

    # 4. In kết quả xuất ra Phiếu khám bệnh điện tử
    print("           PHIẾU KHÁM BỆNH ĐIỆN TỬ")
    print("-" * 50)
    print(f"Tên bệnh nhân      : {patient_name}")
    print(f"Tuổi bệnh nhân     : {patient_age}")
    print(f"Kết quả phân luồng : {classification}")
    print("==================================================")