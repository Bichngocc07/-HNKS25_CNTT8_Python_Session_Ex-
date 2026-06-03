# Chuỗi giao dịch thô ban đầu
transaction = "   nguyeN vaN a | PYTHON-01 | 15000000 | paid  "

# Bước 1: Cắt chuỗi theo đúng ký tự phân tách là dấu '|'
parts = transaction.split("|")

# Bước 2: Lấy từng phần tử, làm sạch khoảng trắng và chuẩn hóa định dạng
student_name = parts[0].strip().title()
course_code = parts[1].strip().upper()

# Bước 3: Ép kiểu tiền số lượng sang số nguyên để định dạng dấu phẩy hàng nghìn
amount_number = int(parts[2].strip())
# Sử dụng f-string định dạng số có dấu phẩy hàng nghìn
formatted_amount = f"{amount_number:,} VND"

status = parts[3].strip().upper()

# Bước 4: In kết quả chuẩn hóa ra màn hình
print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền :", formatted_amount)
print("Trạng thái:", status)