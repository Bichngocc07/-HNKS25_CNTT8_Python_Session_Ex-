students_grades = [
    ["An", [8.5, 9.0, 8.0]],
    ["Binh", [7.0, 6.5, 7.5]],
    ["Chi", [9.5, 10.0, 9.0]]
]

print("--- BÁO CÁO KẾT QUẢ HỌC TẬP ---")

for student in students_grades:
    name = student[0]        
    grades = student[1]      
    
    average_score = sum(grades) / len(grades)
    
    average_score = round(average_score, 1)
    
    if average_score >= 9.0:
        rank = "Xuất sắc"
    elif average_score >= 8.0:
        rank = "Giỏi"
    elif average_score >= 6.5:
        rank = "Khá"
    else:
        rank = "Trung bình"
        
    print(f"Học viên: {name}")
    print(f" - Điểm TB: {average_score}")
    print(f" - Xếp loại: {rank}")
    print("-" * 30)
