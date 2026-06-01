print("--- HỆ THỐNG BÁO CÁO DOANH THU CHI NHÁNH ---")

branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

print("\n--- BẮT ĐẦU NHẬP LIỆU ---")

for branch in range(1, branch_count + 1):
    
    for month in range(1, month_count + 1):
        
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))
        
        print(f"=> Kết quả hiển thị: Chi nhánh {branch}, tháng {month}: {revenue} triệu đồng\n")

print("--- QUÁ TRÌNH LẬP BÁO CÁO HOÀN THÀNH ---")
