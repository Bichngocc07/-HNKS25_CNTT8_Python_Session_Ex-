age = int(input("Nhập tuổi bệnh nhân :"))
systolic_lood_pressure = int(input("Nhập huyết áp tâm thu: "))
blood_sugar = int(input("nhập đường huyết: "))

infomaton = f"""
    --- ĐỦ ĐIỀU KIỆN PHẪU THUẬT ---
    Tuổi : {age}
    Huyết áp tâm thu : {systolic_lood_pressure}
    Đường huyết : {blood_sugar}
"""

if age < 75 and systolic_lood_pressure > 90 and systolic_lood_pressure < 140 and blood_sugar < 150:
    print(infomaton)
else:
    print("TỪ CHỐI PHẪU THUẬT")
