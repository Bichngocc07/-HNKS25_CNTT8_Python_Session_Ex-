print(' --- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN --- ')
name_patient = input('Mời bạn nhập tên bệnh nhân: ')
age = int(input('Mời bạn nhập tuổi: '))
symptom = input('Mời bạn nhập triệu chứng bệnh: ')

print(' -- PHIẾU KHÁM BỆNH --- ')
# Sửa lại các biến cho đúng vị trí logic
print('Tên bệnh nhân:', name_patient)
print('Tuổi:', age)
print('Triệu chứng:', symptom)

# 1. Phân Tích Lỗi (Bug Analysis)
# Dò luồng thực thi (Trace code)
# Bước 1 (Nhập liệu):
# Hệ thống yêu cầu nhập họ tên bệnh nhân và lưu vào biến name_patient
# Hệ thống yêu cầu nhập tuổi và lưu vào biến age (Ví dụ: 25).
# Hệ thống yêu cầu nhập triệu chứng và lưu vào biến symptom 

# Bước 2 (In kết quả):
# Lệnh print('Tên bệnh nhân:', symptom) được thực thi. Lúc này, hệ thống lấy giá trị của biến 
# symptom ("Đau đầu") để in ra sau chữ "Tên bệnh nhân:".
# Lệnh print('Tuổi:', name_patient) được thực thi. Hệ thống lấy giá trị của biến name_patient
# ("Nguyễn Văn A") để in ra sau chữ "Tuổi:".
# Lệnh print('Triệu chứng:', age) được thực thi. Hệ thống lấy giá trị của biến age (25) để 
# in ra sau chữ "Triệu chứng:".

# Nguyên nhân gây lỗi logic
# Lỗi xảy ra do sự nhầm lẫn (tráo đổi) vị trí của các biến trong các câu lệnh print ở phần xuất kết quả:
# Nhãn 'Tên bệnh nhân:' lại đi kèm với biến symptom.
# Nhãn 'Tuổi:' lại đi kèm với biến name_patient.
# Nhãn 'Triệu chứng:' lại đi kèm với biến age.