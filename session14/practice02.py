#Các loại tham số
#Tham số thông thường
def det_student(name, age, school):
    print(f"{name} | {age} | {school}")
    get_student_1("Ngoc",25,"PTIT")

#Tham số mặc định
#NẾU MÀ KHÔNG CÓ ĐỐI SỐ => TRUYỀN MẶC ĐỊNH GIÁ TRỊ KHỞI TẠO THAM SỐ
#NẾU MÀ CÓ ĐỐI SỐ => LẤY GIÁ TRỊ ĐỐI SỐ MỚI ĐÓ
def get_student_2(name = "Tung", age = 18, school = "PTIT"):
    print(f"{name} | {age} | {school}")
get_student_2("Ngọc", 20,"PTIT")

#THAM SỐ TỪ KHÓA
def get_student_3(name,age,school):
    print(f"{name} | {age} | {school}")
get_student_3(age = 17, school ="PTIT", name = "Ngọc")

#THAM SỐ ARGS
def get_all_information_in_company(name, age, room):
    print(f"{name} | {age} | {room}")

#TRƯỜNG HỢP CỦA NHÂN VIÊN
get_all_information_in_company("Ngọc",25,"IT")

#TRƯỜNG HỢP TRƯỞNG PHÒNG
get_all_information_in_company("Ngọc",30,"TechLead",3, 7)