# #Vòng lặp for
# # for index in list/string/range()/tuple/dict:
# #     #block code
# # range(): Tạo ra 1 dãy số nguyên. Lưu ý: range(1,5) => 1,2,3,4 
# for value in range(1,11)
#     print(value)
# #Dùng range() chỉ cho tham số là stop: Nếu không sử dụng start thì mặc định sẽ là 0
# for value in range(11):
#     print(value)

# #in ra các số chẵn từ 0 đến 10
# for value in range(0,11,2):
#     print(value)

# #in ra các số lẻ từ 1 đến 10


# #Tính tổng các số từ 1 đến 10
# total = 0
# #Tạo 1 dãy số từ 1 đến 10
# for value in range(1,11):
# #Cộng dồn các số trong dãy số đó lại với nhau
# total += value
# print(f"total = {total}")

# print("-----Vòng lặp while-----")
# while condition:
#     #block code
#     #Tăng giá trị của biến khởi tạo làm điều kiện
#     #in ra các số từ 1 đến 10 = while
#     while initial_value <= 10:
#         print(initial_value)
# #Tăng giá trị của initial_value lên 1 đơn vị
#         initial_value += 1
# #Xây dựng ứng dụng đăng nhập , cho phép người dùng nhập mk toi đa 3 lần, nếu nhập đúng thì in 
# # ra "Đăng nhập thành công", nếu nhập sai quá 3 lần thì in ra "Tài khoản bị khóa"

# #Mk đúng
# password = "123456"
# #Biến phát hiện khi nào người dùng nhập đúng mk
# isSuccess = False

# # Điều kiện dừng
# while not isSuccess:
#     password_input = input("Nhập mật khẩu: ")

# #Logic xử lý
#     if password_input == password:
#         print("Đăng nhập thành công")
#         isSuccess = True
#     else:
#         print("Mật khẩu sai, vui lòng thử lại")
#     #Tăng biến đếm số lần nhập sai lên 1 đơn vị
#     couter_login_failed += 1
#     #Tạo ứng dụng in ra bảng cửu chương từ 2 đến 9(dùng for)
#     for first_value in range(2,10):
#         print(f"Bảng cửu chương {first_value}")
#     #Tạo ra dãy số từ 1 đến 10
#     for second_value  in range (1,11):
#         print(f"{first_value} x {second_value} = {first_value * second_value}")
# total = 0
# for i in range(1, 5):
#     total = total + i * 2
# print(total)
i = 5
# while i > 0:
#     print(i)
#     i = i + 1
# for i in range(1, 4):
#     print(i)
# print("Xong")
count = 1
# while count <= 3:
#     print(count)
#     count = count + 1
x = 3
while x <= 20:
    x = x * 2
print(x)