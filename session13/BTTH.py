danh_sach_nhan_vien = []

while True:
    print("\n" + "="*35)
    print("QUẢN LÝ NHÂN SỰ - STAFF MANAGER")
    print("="*35)
    print("1. Thêm nhân viên mới")
    print("2. Danh sách nhân viên")
    print("3. Xóa nhân viên khỏi hệ thống")
    print("4. Thoát chương trình")
    print("="*35)

    choice = input("Nhập lựa chọn của bạn: ").strip()
# Chức năng 1:
    if choice == "1":
        print("\n--- THÊM NHÂN VIÊN MỚI ---")

        while True:
            ma_nv = input("Nhập mã nhân viên: ").strip()
            if not ma_nv:
                print("Mã nhân viên không được để trống!")
                continue
            trung = False
            for i in danh_sach_nhan_vien:
                if i['id'] == ma_nv:
                    trung = True
                    break
            if trung:
                print(f"Mã ID '{ma_nv}' đã tồn tại! Vui lòng nhập mã khác.")
            else:
                break
        while True:
            ten_nv = input("Nhập họ và tên nhân viên: ").strip()
            if ten_nv:
                break
            print("Họ tên không được để trống!")
        while True:
            luong_input = input("Nhập mức lương của nhân viên: ").strip()
            luong = int(luong_input)
            if luong > 0:
                break
            else:
                print("Lương phải là số lớn hơn 0!")
        nhan_vien_moi = {
            "id": ma_nv,
            "name": ten_nv,
            "luong": luong
        }
        danh_sach_nhan_vien.append(nhan_vien_moi)
        print(f"Thêm thành công nhân viên: {ten_nv} (ID: {ma_nv})")
