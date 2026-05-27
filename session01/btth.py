user_name = input("Nhập tên bệnh nhân: ")
gender = input("Nhập giới tính của bệnh nhân (Nam/Nữ): ")
date_birth = input("Nhập ngày sinh của bệnh nhân (dd/mm/yyyy): ")
phone_number = input("Nhập số điện thoại của bệnh nhân: ")
email = input("Nhập email của bệnh nhân: ")
symptoms = input("Nhập triệu chứng của bệnh nhân: ")
cost = float(input("Nhập chi phí điều trị của bệnh nhân: "))

#ÉP kiểu dữ liệu
#Tạo mã bệnh nhân ngẫu nhiên
code = f"NV{date_birth}001"

#In ra màn hình
# infomation = f"Mã bệnh nhân: {code}\nTên bệnh nhân: {user_name}\n Giới tính: {gender}"
infomation = f"""
Mã bệnh nhân: {code}
Tên bệnh nhân: {user_name}
Giới tính: {gender}
"""
print(infomation)