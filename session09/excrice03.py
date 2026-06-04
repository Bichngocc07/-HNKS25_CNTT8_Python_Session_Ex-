# 1. Khởi tạo danh sách học viên và điểm số
students_grades = [
    ["An", [8.5, 9.0, 8.0]],
    ["Binh", [7.0, 6.5, 7.5]],
    ["Chi", [9.5, 10.0, 9.0]]
]

print("--- BÁO CÁO KẾT QUẢ HỌC TẬP ---")

# 2. Duyệt qua từng học viên trong danh sách
for student in students_grades:
    name = student[0]          # Lấy tên (phần tử index 0)
    grades = student[1]        # Lấy danh sách điểm (phần tử index 1)
    
    # 3. Tính điểm trung bình
    average_score = sum(grades) / len(grades)
    
    # Làm tròn điểm trung bình đến 1 chữ số thập phân
    average_score = round(average_score, 1)
    
    # 4. Phân loại học lực
    if average_score >= 9.0:
        rank = "Xuất sắc"
    elif average_score >= 8.0:
        rank = "Giỏi"
    elif average_score >= 6.5:
        rank = "Khá"
    else:
        rank = "Trung bình"
        
    # In kết quả cho từng học viên
    print(f"Học viên: {name}")
    print(f" - Điểm TB: {average_score}")
    print(f" - Xếp loại: {rank}")
    print("-" * 30)