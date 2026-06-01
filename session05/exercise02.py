print("--- HỆ THỐNG BÁO CÁO DOANH THU CHI NHÁNH ---")

# Nhập số lượng chi nhánh từ bàn phím
branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

print("\n--- BẮT ĐẦU NHẬP LIỆU ---")

# ĐÚNG NGHIỆP VỤ: Vòng lặp ngoài duyệt theo từng CHI NHÁNH
for branch in range(1, branch_count + 1):
    
    # Vòng lặp trong duyệt tuần tự từng THÁNG của chi nhánh đó
    for month in range(1, month_count + 1):
        
        # Nhập dữ liệu doanh thu trực tiếp
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        
        # Hiển thị trực tiếp dòng báo cáo chuẩn hóa theo đúng định dạng yêu cầu
        print(f"=> Kết quả hiển thị: Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng\n")

print("--- QUÁ TRÌNH LẬP BÁO CÁO HOÀN THÀNH ---")