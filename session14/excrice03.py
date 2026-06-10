
students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]
while True:
    print("====== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY ======")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")
    print("======================================================")
    
    choice = input("> Mời chọn chức năng (1-5): ").strip()
    
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!\n")
        continue
        
    if choice == "1":
        display_students(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        update_score(students)
    elif choice == "4":
        evaluate_students(students)
    elif choice == "5":
        print("\nCảm ơn bạn đã sử dụng hệ thống!")
        print("Cổng điều hướng Rikkei Academy đã đóng an toàn.")
        break



def validate_score(score_input):
    """Kiểm tra điểm số nhập vào có phải số thực hợp lệ từ 0 đến 10 hay không."""
    if score_input.replace(".", "", 1).isdigit():
        score = float(score_input)
        if 0 <= score <= 10:
            return True
    return False

def find_student_by_id(student_list, student_id):
    """Tìm kiếm vị trí (index) của học viên trong danh sách theo mã ID.
    Trả về index nếu tìm thấy, ngược lại trả về -1.
    """
    for i in range(len(student_list)):
        if student_list[i]["student_id"] == student_id:
            return i
    return -1

def get_rank(average_score):
    """Phân loại học lực dựa trên điểm trung bình."""
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

# =========================================================================
# CÁC HÀM CHỨC NĂNG CHÍNH (MAIN FUNCTIONS)
# =========================================================================

def display_students(student_list):
    """Chức năng 1: Hiển thị danh sách học viên hiện tại."""
    print("\n--- DANH SÁCH HỌC VIÊN ---")
    if len(student_list) == 0:
        print("Danh sách học viên hiện đang trống.")
    else:
        for i in range(len(student_list)):
            s = student_list[i]
            print(f"{i + 1}. Mã: {s['student_id']} | Tên: {s['name']} | Toán: {s['math_score']} | Anh: {s['english_score']}")
    print("")

def add_student(student_list):
    """Chức năng 2: Tiếp nhận thông tin và thêm học viên mới vào hệ thống."""
    print("\n--- THÊM HỌC VIÊN MỚI ---")
    
    # Bẫy 1 & Chuẩn hóa mã học viên
    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()
        if not student_id:
            print("Mã học viên không được để trống!")
            continue
            
        # Gọi helper function kiểm tra trùng mã
        if find_student_by_id(student_list, student_id) != -1:
            print(f"Lỗi: Mã học viên '{student_id}' đã tồn tại, vui lòng nhập mã khác!")
            continue
        break

    # Bẫy 4: Chặn họ tên trống
    while True:
        name = input("Nhập tên học viên: ").strip()
        if not name:
            print("Tên học viên không được để trống!")
            continue
        # Chuẩn hóa viết hoa chữ cái đầu từng từ (Title Case)
        name = name.title()
        break

    # Bẫy 2: Chặn điểm rác cho môn Toán
    while True:
        math_input = input("Nhập điểm Toán: ").strip()
        if validate_score(math_input):
            math_score = float(math_input)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10! Vui lòng nhập lại.")

    # Bẫy 2: Chặn điểm rác cho môn Tiếng Anh
    while True:
        english_input = input("Nhập điểm Tiếng Anh: ").strip()
        if validate_score(english_input):
            english_score = float(english_input)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10! Vui lòng nhập lại.")

    # Đóng gói Dictionary nạp vào cơ sở dữ liệu mảng
    new_student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    }
    student_list.append(new_student)
    print("Thêm học viên thành công!\n")

def update_score(student_list):
    
