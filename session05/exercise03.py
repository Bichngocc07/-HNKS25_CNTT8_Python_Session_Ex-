# 1. Nhập số lượng chi nhánh và số lượng lớp học của mỗi chi nhánh
branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lượng lớp học tại mỗi chi nhánh: "))
print("") # Dòng trống phân cách

# Vòng lặp ngoài: Duyệt qua từng chi nhánh của trung tâm
for branch in range(1, branch_count + 1):
    print(f"--- Đang xử lý Chi nhánh {branch} ---")
    
    # ĐÚNG LOGIC: Mỗi khi chuyển sang chi nhánh mới, tổng học viên phải reset về 0
    total_students = 0
    
    # Vòng lặp trong: Duyệt qua từng lớp học của chi nhánh hiện tại để thu thập dữ liệu
    for classroom in range(1, class_count + 1):
        students_count = int(input(f"   Nhập số học viên lớp {classroom}: "))
        # Cộng dồn học viên của các lớp vào tổng riêng của chi nhánh đó
        total_students += students_count
        
    # In ra báo cáo tổng số học viên của riêng chi nhánh này
    print(f"==> Chi nhánh {branch}: {total_students} học viên")
    print("-" * 40) # Gạch gãy dòng phân cách giữa các chi nhánh