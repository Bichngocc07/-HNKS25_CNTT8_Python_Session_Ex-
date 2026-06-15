# =============================================================================
# CẤU TRÚC DỮ LIỆU BAN ĐẦU
# =============================================================================
# Khởi tạo danh sách 'student_list' chứa thông tin sinh viên dưới dạng một List.
# Bên trong List này chứa các từ điển (Dictionary). Mỗi sinh viên là một đối tượng
# có các khoá (key) rõ ràng để quản lý thông tin.
student_list = [
    {"id": "SV001",
     "name":"Nguyen Van A",
     "Toán": 8.5,
     "Lý": 7.0,
     "Hóa": 9.0,
     "Điểm trung bình": 8.17,
     "Xếp loại học lực": "Giỏi"}
]

# =============================================================================
# ĐỊNH NGHĨA CÁC HÀM CHỨC NĂNG (ĐẶT Ở TRÊN)
# =============================================================================

# CHỨC NĂNG 1: HIỂN THỊ DANH SÁCH SINH VIÊN
def play_student():
    print("--- HIỂN THỊ DANH SÁCH SINH VIÊN ---")
        
    # Sử dụng hàm len() kiểm tra số lượng phần tử. Nếu bằng 0 tức là danh sách rỗng.
    if len(student_list) == 0:
        print("HỆ THÔNG CHƯA CÓ SINH VIÊN NÀO!!!")
    else:
        # In tiêu đề các cột của bảng hiển thị
        print(f" {'Mã SV'}  {'Họ và Tên'}  {'Toán'}      {'Lý'}       {'Hóa'}       {'ĐTB'}  {'Xếp Loại'} ")
        
    # Vòng lặp for duyệt qua từng sinh viên (đối tượng sv) trong danh sách để bóc tách dữ liệu
    for sv in student_list:
        print(f" {sv['id']} {sv['name']} {sv['Toán']}    {sv['Lý']}   {sv['Hóa']}   {sv['Điểm trung bình']}  {sv['Xếp loại học lực']} ")


# CHỨC NĂNG 2: TIẾP NHẬN SINH VIÊN MỚI
def add_student():
    print("\n--- TIẾP NHẬN SINH VIÊN MỚI ---")
    
    # Sử dụng vòng lặp while True vô hạn để bắt người dùng nhập mã hợp lệ mới cho đi tiếp
    while True:
        # .strip() để xóa khoảng trắng thừa, .upper() để tự động chuyển thành chữ in hoa
        sv_id = input("Nhập mã sinh viên (không được rỗng): ").strip().upper()
        
        # Kiểm tra nếu người dùng bỏ trống không nhập gì
        if not sv_id:
            print("Mã sinh viên không được để rỗng!")
            continue # Lệnh continue ép vòng lặp quay lại từ đầu để bắt nhập lại
            
        # Kiểm tra thuật toán trùng mã sinh viên trong hệ thống
        trung_ma = False
        for sv in student_list:
            if sv["id"] == sv_id:
                trung_ma = True
                break # Nếu phát hiện trùng thì dừng vòng lặp duyệt danh sách ngay lập tức
                
        if trung_ma:
            print(f"Mã SV '{sv_id}' đã tồn tại! Vui lòng nhập mã khác.")
        else:
            break # Mã hợp lệ và không trùng thì bẻ gãy vòng lặp while để chuyển sang bước sau


# CHỨC NĂNG 3: CẬP NHẬT KẾT QUẢ HỌC TẬP
def update_student():
    print("\n--- CẬP NHẬT KẾT QUẢ HỌC TẬP ---")
    sv_id = input("Nhập mã sinh viên cần sửa điểm: ").strip().upper()
    
    found = False # Biến cờ hiệu (flag) đánh dấu trạng thái tìm thấy sinh viên, ban đầu là False
    for sv in student_list:
        if sv["id"] == sv_id:
            found = True # Đổi trạng thái thành True khi tìm thấy mã trùng khớp
            print(f"Sửa điểm cho sinh viên: {sv['name']}")
            
            # Hàm nội bộ (sub-function) giúp kiểm tra và bắt lỗi nhập điểm từ 0 đến 10
            def nhap_diem_moi(ten_mon):
                while True:
                    try:
                        diem = float(input(f"Nhập điểm {ten_mon} mới: "))
                        if 0 <= diem <= 10:
                            return diem # Điểm hợp lệ thì trả giá trị về và thoát hàm phụ này
                        print("Điểm phải từ 0 đến 10!")
                    except ValueError:
                        # Khối except này ngăn chương trình bị dừng đột ngột (crash) khi người dùng nhập chữ
                        print("Vui lòng nhập số thực hợp lệ.")

            # Gọi hàm phụ ở trên và gán đè điểm mới vào trực tiếp các Key của dictionary sinh viên đó
            sv["Toán"] = nhap_diem_moi("Toán")
            sv["Lý"] = nhap_diem_moi("Lý")
            sv["Hóa"] = nhap_diem_moi("Hóa")

            # Thực hiện tính lại Điểm trung bình (lấy 2 chữ số thập phân bằng hàm round)
            sv["Điểm trung bình"] = round((sv["Toán"] + sv["Lý"] + sv["Hóa"]) / 3, 2)
            
            # Cấu trúc rẽ nhánh kiểm tra điểm trung bình để xếp lại học lực theo quy định đề bài
            if sv["Điểm trung bình"] < 5.0:
                sv["Xếp loại học lực"] = "Yếu"
            elif sv["Điểm trung bình"] < 7.0:
                sv["Xếp loại học lực"] = "Trung bình"
            elif sv["Điểm trung bình"] < 8.0:
                sv["Xếp loại học lực"] = "Khá"
            else:
                sv["Xếp loại học lực"] = "Giỏi"
            print("Cập nhật kết quả thành công!")
            break # Sửa xong sinh viên cần tìm thì bẻ gãy vòng lặp for để kết thúc
            
    # Nếu chạy hết vòng lặp quét danh sách mà biến found vẫn là False thì báo lỗi cho người dùng
    if not found:
        print(f"Không tìm thấy mã sinh viên '{sv_id}'.")


# CHỨC NĂNG 4: XÓA SINH VIÊN
def delete_student():
    print("\n--- XÓA SINH VIÊN ---")
    sv_id = input("Nhập mã sinh viên cần xóa: ").strip().upper()
    
    target_sv = None # Biến tạm dùng để lưu trữ đối tượng sinh viên tìm được để xóa
    for sv in student_list:
        if sv["id"] == sv_id:
            target_sv = sv # Tìm thấy sinh viên trùng mã thì gán vào biến tạm
            break
            
    if target_sv:
        # Đưa ra thông báo hỏi lại để xác nhận hành động xóa nhằm bảo vệ an toàn dữ liệu
        confirm = input(f"Bạn có chắc chắn muốn xóa SV {target_sv['name']} không? (Y/N): ").strip().upper()
        if confirm == "Y":
            student_list.remove(target_sv) # Sử dụng phương thức .remove() để loại bỏ hẳn dictionary khỏi List
            print("Đã xóa sinh viên khỏi hệ thống thành công.")
        else:
            print("Đã hủy thao tác xóa.")
    else:
        print(f"Không tìm thấy mã sinh viên '{sv_id}'.")


# CHỨC NĂNG 5: TÌM KIẾM SINH VIÊN
def search_student():
    print("\n--- TÌM KIẾM SINH VIÊN ---")
    print("1. Tìm chính xác theo mã SV")
    print("2. Tìm gần đúng theo tên SV")
    kieu_tim = input("Chọn kiểu tìm kiếm (1-2): ").strip()
    
    ket_qua = [] # Khởi tạo danh sách phụ để lưu trữ các kết quả tìm thấy
    if kieu_tim == "1":
        ma_tim = input("Nhập mã sinh viên cần tìm: ").strip().upper()
        # List Comprehension quét toàn bộ danh sách để tìm sinh viên khớp chính xác mã định danh
        ket_qua = [sv for sv in student_list if sv["id"] == ma_tim]
    elif kieu_tim == "2":
        ten_tim = input("Nhập tên sinh viên cần tìm: ").strip().lower()
        # Tìm kiếm gần đúng: Dùng toán tử 'in' để kiểm tra chuỗi con và hàm .lower() để không phân biệt chữ HOA-thường
        ket_qua = [sv for sv in student_list if ten_tim in sv["name"].lower()]
    else:
        print("Lựa chọn không hợp lệ!")
        return # Dùng lệnh return để thoát hàm tìm kiếm ngay lập tức khi chọn sai kiểu

    # Kiểm tra độ dài danh sách chứa kết quả thu được để hiển thị thông báo ra màn hình
    if len(ket_qua) == 0:
        print("🔍 Không tìm thấy sinh viên nào phù hợp!")
    else:
        print(f"\n🔍 Đã tìm thấy {len(ket_qua)} kết quả phù hợp:")
        print(f"| {'Mã SV':<8} | {'Họ và Tên':<20} | {'Toán':<5} | {'Lý':<5} | {'Hóa':<5} | {'ĐTB':<5} | {'Xếp Loại':<10} |")
        print("-" * 75)
        for sv in ket_qua:
            print(f"| {sv['id']:<8} | {sv['name']:<20} | {sv['Toán']:<5.1f} | {sv['Lý']:<5.1f} | {sv['Hóa']:<5.1f} | {sv['Điểm trung bình']:<5.2f} | {sv['Xếp loại học lực']:<10} |")


# CHỨC NĂNG 6: THỐNG KÊ ĐIỂM TRUNG BÌNH
def statistics_student():
    print("\n--- THỐNG KÊ ĐIỂM TRUNG BÌNH & HỌC LỰC ---")
    if len(student_list) == 0:
        print("Chưa có sinh viên nào để thống kê.")
        return
        
    # Tạo từ điển đếm với giá trị ban đầu bằng 0 cho từng danh mục xếp loại học lực
    thong_ke = {"Giỏi": 0, "Khá": 0, "Trung bình": 0, "Yếu": 0}
    for sv in student_list:
        xl = sv["Xếp loại học lực"]
        if xl in thong_ke:
            thong_ke[xl] += 1 # Duyệt qua sinh viên thuộc nhóm nào thì cộng dồn thêm 1 vào nhóm đó
            
    print("-" * 35)
    print(f"| {'Xếp loại học lực':<18} | {'Số lượng':<10} |")
    print("-" * 35)
    # Lặp qua các cặp Key-Value trong từ điển thống kê để in báo cáo số liệu
    for rank, count in thong_ke.items():
        print(f"| {rank:<18} | {count:<10} |")
    print("-" * 35)
    print(f" Tổng số sinh viên hiện tại: {len(student_list)}")


# CHỨC NĂNG 7: PHÂN LOẠI HỌC LỰC
def classify_student():
    print("\n--- TIẾN HÀNH PHÂN LOẠI HỌC LỰC TOÀN BỘ DANH SÁCH ---")
    if len(student_list) == 0:
        print("Danh sách rỗng, không thể phân loại.")
        return
        
    # Duyệt vòng lặp chạy qua toàn bộ sinh viên trong hệ thống để thực hiện rà soát và đồng bộ hóa lại xếp loại học lực
    for sv in student_list:
        sv["Điểm trung bình"] = round((sv["Toán"] + sv["Lý"] + sv["Hóa"]) / 3, 2)
        dtb = sv["Điểm trung bình"]
        if dtb < 5.0:
            sv["Xếp loại học lực"] = "Yếu"
        elif dtb < 7.0:
            sv["Xếp loại học lực"] = "Trung bình"
        elif dtb < 8.0:
            sv["Xếp loại học lực"] = "Khá"
        else:
            sv["Xếp loại học lực"] = "Giỏi"
            
    print("Đã rà soát, tự động cập nhật lại ĐTB và Xếp loại cho toàn bộ sinh viên!")


# =============================================================================
# VÒNG LẶP ĐIỀU KHIỂN CHƯƠNG TRÌNH (ĐẶT Ở DƯỚI)
# =============================================================================
# Vòng lặp while True chạy vô hạn duy trì giao diện menu CLI luôn hiển thị liên tục 
# sau khi người dùng thực hiện xong một chức năng.
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
    
    # Sử dụng cấu trúc rẽ nhánh if - elif - else để so sánh giá trị chuỗi nhập vào biến choice
    # và kích hoạt gọi hàm xử lý chức năng tương ứng tương đương ở trên.
    if choice == "1":
        play_student()
    elif choice == "2":
        add_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        search_student()
    elif choice == "6":
        statistics_student()
    elif choice == "7":
        classify_student()
    elif choice == "8":
        print("ĐÃ THOÁT CHƯƠNG TRÌNH !")
        break # Thực thi câu lệnh break bẻ gãy vòng lặp while True, ngắt và chấm dứt ứng dụng CLI hoàn toàn
    else:
        # Xử lý trường hợp người dùng nhập ký tự không hợp lệ nằm ngoài dải số từ 1 đến 8
        print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 8.")
