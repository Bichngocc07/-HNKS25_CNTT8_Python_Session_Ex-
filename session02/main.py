#Toán tử số học
first_number = 20
second_number = 30

print(f"({first_number} + {second_number}) = {first_number + second_number}")
print(f"({first_number} - {second_number}) = {first_number - second_number}")
print(f"({first_number} * {second_number}) = {first_number * second_number}")

print(f"({first_number} / {second_number}) = {first_number / second_number}")
# Toán tử chia lấy phần nguyên
print(f"({first_number} // {second_number}) = {first_number // second_number}")
# Toán tử chia lấy phần dư
print(f"({first_number} % {second_number}) = {first_number % second_number}")
print(f"({first_number} > {second_number}) = {first_number > second_number}")#FALSE
print(f"({first_number} < {second_number}) = {first_number < second_number}")#TRUE
print(f"({first_number} >= {second_number}) = {first_number >= second_number}")
print(f"({first_number} != {second_number}) = {first_number != second_number}")


#Toán tử logic
#Trong python sẽ có một giá trị mặc định là False: Số 0, False, "", [], (), {}
first_result = 20 > 10 and 30 > 20 and 100
second_result = 20 > 10 or 30 < 20 or 100


print(f"Result: {first_result}")
print(f"Result: {second_result}")
print(f"not của second_result là: {not second_result}")

#Cấu trúc điều kiện
#1. Trường hợp bài toán có 1 điều kiện duy nhất
#Lưu ý là trong python để thể hiện 1 block code thì dùng tag thay thế cho{}
age = 18
if age >= 18:
    print("Bạn đã đủ tuổi để thi bằng lái xe ")
#2. Trường hợp bài toán có 2 điều kiện
gender = "MALE"
if gender == "MALE":
    print("Giới tính nam")
else:
    print("Giới tính nữ")
#3. Trường hợp bài toán có nhiều hơn 2 điều kiện và điều kiện phải nằm trong 1 khoảng
avg_point = 8.5
#Kiểm tra học lực của sinh viên
if avg_point >= 9 and avg_point <= 10:
    print("Học lực xuất sắc")
elif avg_point >= 8 and avg_point < 9:
    print("Học lực giỏi")
elif avg_point >= 6.5 and avg_point < 8:
    print("Học lực khá")
elif avg_point >= 5 and avg_point < 6.5:
    print("Học lực trung bình")
else:
    print("Học lực yếu")

#MATCH CASE
status = "ACTIVE" #ACTIVE,INACTIVE,PAUSE_ACTIVE
match status:
    case "ACTIVE":
        print("Trạng thái đang hoạt động")
    case "INACTIVE":
        print("Trạng thái không hoạt động")
    case "PAUSE_ACTIVE":
        print("Trạng thái tạm ngưng hoạt động")
    case _:
        print("Trạng thái không hợp lệ")
#Điều kiện lồng nhau
#Kiểm tra điều kiện thi bằng lái xe : tuổi > 18, độ cận < 3
my_age = 18
nearsightedness = 5
if my_age >= 18:
    #Tiếp tục kiểm tra độ cận
    if nearsightedness < 3:
        print("Bạn đủ để thi nhưng độ cận cao, Kết luận không đạt")
    else:
        print("Bạn đủ điều kiện thi")
else:
    print("Bạn chưa đủ tuổi để thi bằng lái xe")
#Toán tử 3 ngôi
#Gender = "FEMALE"
#if gender == "MALE":
#"print("Gioiws tính nam")
#else:
#    print("Giới tính nữ")
print(f"{'Nam' if gender == 'MALE' else 'Nữ'}")
# print("Hello")
# name = "An"
# print(f"Xin chao {name}")
# status = "OK" result = "Pass" if status == "OK" else "Fail" print(result)
