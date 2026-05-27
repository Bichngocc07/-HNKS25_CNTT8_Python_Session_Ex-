print("     HỆ THỐNG SÀNG LỌC ĐIỀU KIỆN PHẪU THUẬT")

# 1. Tiếp nhận dữ liệu đầu vào và ép kiểu dữ liệu
age = int(input("Nhập tuổi bệnh nhân: "))
sbp = int(input("Nhập huyết áp tâm thu (mmHg): "))
blood_sugar = int(input("Nhập chỉ số đường huyết (mg/dL): "))

print("\n" + "-"*50)
print("               KẾT QUẢ SÀNG LỌC")
print("-" * 50)

# 2. Xử lý Edge Cases: Nhận diện dữ liệu âm hoặc không hợp lệ (nhỏ hơn hoặc bằng 0)
if age <= 0 or sbp <= 0 or blood_sugar <= 0:
    print("Thông báo lỗi: Dữ liệu nhập vào không hợp lệ")
    print("Vui lòng kiểm tra lại các chỉ số sinh hiệu (Không được <= 0).")

else:
    # 3. Phân tích điều kiện y khoa (Nested Logic / Chi tiết hóa lý do)
    # Khởi tạo danh sách chứa các tiêu chí bị vi phạm (nếu có)
    reasons_for_rejection = []

    # Kiểm tra tiêu chí 1: Tuổi
    if age >= 75:
        reasons_for_rejection.append(f"Tuổi không đạt ({age} tuổi >= 75)")

    # Kiểm tra tiêu chí 2: Huyết áp tâm thu
    if sbp < 90 or sbp > 140:
        reasons_for_rejection.append(f"Huyết áp tâm thu nằm ngoài vùng an toàn ({sbp} mmHg)")

    # Kiểm tra tiêu chí 3: Đường huyết
    if blood_sugar >= 150:
        reasons_for_rejection.append(f"Đường huyết vượt ngưỡng an toàn ({blood_sugar} mg/dL)")

    # 4. Đưa ra kết luận dựa trên danh sách vi phạm
    if len(reasons_for_rejection) == 0:
        print("KẾT LUẬN: ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
        print("Bệnh nhân đủ an toàn để tiến hành lên bàn mổ.")
    else:
        print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
        print("Lý do vi phạm chi tiết:")
        for reason in reasons_for_rejection:
            print(f"  - {reason}")