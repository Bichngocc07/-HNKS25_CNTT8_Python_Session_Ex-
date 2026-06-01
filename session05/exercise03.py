branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lượng lớp học tại mỗi chi nhánh: "))
print("") 
for branch in range(1, branch_count + 1):
    print(f"--- Đang xử lý Chi nhánh {branch} ---")
    
    total_students = 0
    
    for classroom in range(1, class_count + 1):
        students_count = int(input(f"   Nhập số học viên lớp {classroom}: "))
        total_students += students_count
        
    print(f"==> Chi nhánh {branch}: {total_students} học viên")
    print("-" * 40)
