print("     MODULE KHỞI TẠO & PHÂN LUỒNG BỆNH ÁN SỐ")

name_input = input("Nhập họ và tên bệnh nhân: ")


patient_age = int(input("Nhập tuổi bệnh nhân: "))

if patient_name == "" or patient_age < 0 or patient_age > 150:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    print("Hệ thống đã chặn dữ liệu rác. Tiến trình phân luồng bị hủy.")
    print("-" * 50)
else:
    if patient_age < 6:
        classification = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
    elif patient_age >= 80:
        classification = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
    else:
        classification = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

    print("           PHIẾU KHÁM BỆNH ĐIỆN TỬ")
    print("-" * 50)
    print(f"Tên bệnh nhân      : {patient_name}")
    print(f"Tuổi bệnh nhân     : {patient_age}")
    print(f"Kết quả phân luồng : {classification}")
    print("==================================================")
