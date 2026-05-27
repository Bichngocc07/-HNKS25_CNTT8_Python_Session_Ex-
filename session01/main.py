# camel case
    # userName = "Nguyen Van B"
# Pascal case
    # UserName = "Nguyen Van C"
# snake case
    # user_name = "Nguyen Van D"
# upper case
    # USER_NAME = "Nguyen Van E"

# khai báo biến bên trong python
user_name = "Nguyen Van A"

print(user_name)

# Kiểu dữ liệu trong python
# int, float, string, boolean, list, tuple, set, dict
    # int : là kiểu dữ liệu số nguyên
AGE = 18
    # float : là kiểu dữ liệu số thực
MATH_SCORE = 9.75
    # string : là kiểu dữ liệu chuỗi
EMAIL = "nva@gmail.com"
    # boolean : là kiểu dữ liệu logic
IS_STUDENT = True
    # list : là kiểu dữ liệu danh sách
    # tuple : là kiểu dữ liệu bộ
    # set : là kiểu dữ liệu tập hợp
    # dict : là kiểu dữ liệu từ điển

# Cơ chế nhập xuất dữ liệu trong python
    # input : cơ chế nhập dữ liệu từ bàn phím
address = input("Vui lòng nhập địa chỉ của bạn: ")
my_age = input("Vui lòng nhập tuổi của bạn: ")
    # print : là hàm xuất dữ liệu ra
print("Địa chỉ của tôi là: ", address)

# Cách kiểm tra kiểu dữ liệu của một biến
print("Kiểu dữ liệu của biến address là: ", type(address))
print("Kiểu dữ liệu của biến my_age là: ", type(my_age))

# Ép kiểu từ chuỗi sang số
new_my_age = int(my_age)
print("Kiểu dữ liệu của biến my_age sau khi đã ép kiểu là: ", type(new_my_age))
# Ép kiểu dữ liệ về boolean
print("my_age sau khi ép về boolean là: ", bool(my_age))

# Trong python, các giá trị mặc định nhận là False: 0, 0.0, ""
print("0 có giá trị boolean là: ", bool(0))
print("0.0 có giá trị boolean là: ", bool(0.0))
print("'' có giá trị boolean là: ", bool(""))

# Cách format chuỗi, nối chuỗi trong python
# In ra chuỗi : Tôi năm nay 20 tuổi, tôi tới từ Hà Nội
# message = "Tôi năm nay " + my_age + " tuổi, tôi tới từ " + address
message = f"Tôi năm nay {my_age} tuổi, tôi tới từ {address}"
print(message)
