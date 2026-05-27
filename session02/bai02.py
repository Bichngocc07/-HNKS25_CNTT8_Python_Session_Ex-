print("--- HỆ THỐNG SÀNG LỌC ĐIỀU KIỆN HIẾN MÁU ---")

# Thu thập dữ liệu đầu vào và ép kiểu chính xác
donor_age = int(input("Nhập tuổi người hiến máu: "))
donor_weight = float(input("Nhập cân nặng người hiến máu (kg): "))

print("\n--- KẾT QUẢ SÀNG LỌC ---")
# Sử dụng toán tử 'and' để bắt buộc thỏa mãn ĐỒNG THỜI cả hai điều kiện
if donor_age >= 18 and donor_weight >= 50:
    print("Kết quả: ĐỦ ĐIỀU KIỆN. Vui lòng di chuyển đến phòng hiến máu.")
else:
    print("Result: KHÔNG ĐỦ ĐIỀU KIỆN. Xin cảm ơn lòng hảo tâm của bạn.")
    print("Lý do từ chối cụ thể:")
    
    # Chỉ ra lý do cụ thể để minh bạch thông tin
    if donor_age < 18:
        print("  - Chưa đạt yêu cầu về độ tuổi (Phải từ 18 tuổi trở lên).")
    if donor_weight < 50:
        print("  - Chưa đạt yêu cầu về cân nặng (Phải từ 50kg trở lên).")

# 1. Phân Tích và Thiết Kế Giải Pháp
# Phân tích Input / Output
# Dữ liệu đầu vào (Input):
# Họ và tên bệnh nhân: Chuỗi ký tự (str).
# Tuổi: Số nguyên (int).
# Dữ liệu đầu ra (Output):
# Nếu dữ liệu hợp lệ: Xuất ra "Phiếu khám bệnh điện tử" bao gồm ba thông tin: Họ tên, Tuổi và Kết quả phân luồng.
# Nếu dữ liệu lỗi (Edge cases): Xuất duy nhất một thông báo cảnh báo lỗi: "LỖI: Tên không hợp lệ hoặc Tuổi nằm 
# ngoài phạm vi con người (0-150)!" và ngắt chương trình.