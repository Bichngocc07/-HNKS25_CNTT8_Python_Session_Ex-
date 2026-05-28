print("==================================================")
print("     MODULE KIOSK NHẬP LIỆU NHÂN SỰ SỐ (BACKEND)")
print("==================================================")

for index in range(1, 4):
    print(f"\n--- ĐANG TIẾP NHẬN NHÂN SỰ THỨ {index} ---")
    
    raw_id = input("Nhập mã nhân viên (Ví dụ: NV001): ")
    raw_name = input("Nhập họ và tên nhân viên: ")
    raw_dept = input("Nhập phòng ban công tác: ")
    
    employee_id = raw_id.strip()
    employee_name = raw_name.strip()
    employee_department = raw_dept.strip()
    
    if employee_id == "" or employee_name == "":
        print("\n[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        print("-" * 50)
        continue
        
    print("\n===================================")
    print("        PHIẾU HỒ SƠ ĐIỆN TỬ")
    print("===================================")
    print(f"Mã nhân viên       : {employee_id}")
    print(f"Họ và tên nhân viên: {employee_name}")
    print(f"Phòng ban công tác : {employee_department}")
    print("===================================")
    print("-> Trạng thái: Đã đồng bộ dữ liệu sang bộ phận IT.")
    print("-" * 50)

print("\nHệ thống phân luồng đã xử lý đủ 3 nhân sự. Chương trình kết thúc.")
