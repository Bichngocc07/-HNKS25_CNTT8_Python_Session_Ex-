student_list = [
    {"id": "SV001",
     "name":"Nguyen Van A",
     "Toán": 8.5,
     "Lý": 7.0,
     "Hóa": 9.0,
     "Điểm trung bình": 8.17,
     "Xếp loại học lực": "Giỏi"}
]
def play_student():
    print("--- HIỂN THỊ DANH SÁCH SINH VIÊN ---")
        
    if len(student_list) == 0:
        print("HỆ THÔNG CHƯA CÓ SINH VIÊN NÀO!!!")
    else:
        print(f" {'Mã SV'}  {'Họ và Tên'}  {'Toán'}      {'Lý'}       {'Hóa'}       {'ĐTB'}  {'Xếp Loại'} ")
    for sv in student_list:
        print(f" {sv['id']} {sv['name']} {sv['Toán']}    {sv['Lý']}   {sv['Hóa']}   {sv['Điểm trung bình']}  {sv['Xếp loại học lực']} ")
            
while True:
    print("-----------------------------------------------")
    print("1. HIỂN THỊ DANH SÁCH SINH VIÊN: ")
    print("2. TIẾP NHẬN SINH VIÊN: ")
    print("3. CẬP NHẬT KẾT QUẢ HỌC TẬP CỦA SINH VIÊN: ")
    print("4. XÓA SINH VIÊN: ")
    print("5. TÌM KIẾM SINH VIÊN : ")
    print("6. THỐNG KÊ ĐIỂM TRUNG BÌNH : ")
    print("7. PHÂN LOẠI HỌC LỰC: ")
    print("8. THOÁT CHƯƠNG TRÌNH : ")
    print("-----------------------------------------------")

    choice = input("Mời bạn chọn chức năng (1-8) : ").strip()
    if choice == "1":
        play_student()
    if choice == "8":
        print("ĐÃ THOÁT CHƯƠNG TRÌNH !")
        break