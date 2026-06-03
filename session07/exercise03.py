transaction = "   nguyeN vaN a | PYTHON-01 | 15000000 | paid  "

parts = transaction.split("|")

student_name = parts[0].strip().title()
course_code = parts[1].strip().upper()

amount_number = int(parts[2].strip())
formatted_amount = f"{amount_number:,} VND"

status = parts[3].strip().upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền :", formatted_amount)
print("Trạng thái:", status)
