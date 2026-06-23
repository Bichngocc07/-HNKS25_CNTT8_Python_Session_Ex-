import os
import math
import re
from datetime import datetime, timedelta

# =============================================================================
# CẤU TRÚC DỮ LIỆU BAN ĐẦU (Dữ liệu mẫu mô phỏng từ API hàng không)
# =============================================================================
flights = [
    {
        "flight_id": "VN301",
        "passengers": 150,
        "depart_time": "2026-06-23 08:00:00",
        "duration_min": 120,
        "status": "Hà Nội - TP.HCM"
    },
    {
        "flight_id": "VN402",
        "passengers": 45,
        "depart_time": "2026-06-23 13:30:00",
        "duration_min": 45,
        "status": "Hà Nội - Vinh"
    }
]


# =============================================================================
# ĐỊNH NGHĨA NGOẠI LỆ TÙY CHỈNH (CUSTOM EXCEPTIONS)
# =============================================================================
class FlightNotFoundError(Exception):
    """Ngoại lệ quăng ra khi không tìm thấy mã chuyến bay trong hệ thống."""
    pass


class InvalidDateTimeError(Exception):
    """Ngoại lệ quăng ra khi định dạng thời gian nhập vào bị sai quy chuẩn."""
    pass


# =============================================================================
# MÔ PHỎNG CÁC PHÂN HỆ CHỨC NĂNG (GỘP MODULES)
# =============================================================================

# --- Phân hệ hệ thống: utils/helper.py ---
def safe_create_directory(dir_name="aviation_logs"):
    """Kiểm tra và tạo thư mục một cách an toàn, bẫy lỗi trùng lặp tên."""
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"[SYSTEM] Thư mục '{dir_name}' chưa tồn tại... Đang tiến hành khởi tạo...")
    print("[SYSTEM] Tạo thư mục thành công!")


# --- Phân hệ nghiệp vụ: core/logistics.py ---
def allocate_flight_sections(passengers):
    """Tính toán số lượng khoang máy bay dựa trên quy chuẩn 50 khách/khoang."""
    # Áp dụng thuật toán làm tròn lên (Ceiling) theo quy tắc của Math
    sections = math.ceil(passengers / 50)
    return sections


# --- Phân hệ nghiệp vụ: core/time.py ---
def calculate_flight_eta(depart_str, duration_min):
    """Phân tích cú pháp chuỗi thời gian khởi hành và dự phóng điểm hạ cánh."""
    # Ép kiểu từ dạng chuỗi văn bản sang đối tượng datetime thực tế để tính toán
    depart_obj = datetime.strptime(depart_str, "%Y-%m-%d %H:%M:%S")
    # Cộng thêm khoảng thời gian bay (duration) bằng timedelta
    eta_obj = depart_obj + timedelta(minutes=int(duration_min))
    return eta_obj


# --- Phân hệ nghiệp vụ: core/manager.py ---
def add_new_flight(flights_list, flight_id, passengers, depart_time, duration_min, status):
    """Đóng gói dữ liệu và tiếp nhận một chuyến bay mới vào danh sách."""
    new_flight = {
        "flight_id": flight_id,
        "passengers": int(passengers),
        "depart_time": depart_time,
        "duration_min": int(duration_min),
        "status": status
    }
    flights_list.append(new_flight)


# =============================================================================
# GIAO DIỆN CONSOLE VÀ LUỒNG ĐIỀU KHIỂN CHƯƠNG TRÌNH
# =============================================================================
def show_aviation_menu():
    """In bảng giao diện menu quản lý lịch trình bay."""
    print("\n====== HỆ THỐNG QUẢN LÝ LỊCH TRÌNH BAY RIKKEI AVIATION ======")
    print("1. Thống kê lịch trình và Thông số máy bay")
    print("2. Tiếp nhận chuyến bay mới")
    print("3. Tính toán giờ hạ cánh dự kiến (ETA)")
    print("4. Khởi tạo thư mục lưu trữ nhật ký hệ thống")
    print("5. Thoát chương trình")
    print("-------------------------------------------------------------")


def main():
    while True:
        show_aviation_menu()
        choice = input("Mời nhập lựa chọn của bạn: ").strip()

        # CHỨC NĂNG 1: THỐNG KÊ LỊCH TRÌNH VÀ THÔNG SỐ
        if choice == "1":
            print("\n----- DANH SÁCH CHUYẾN BAY & HIỆU SUẤT -----")
            for fl in flights:
                # Tính toán số khoang máy bay cần trưng dụng
                sections = allocate_flight_sections(fl["passengers"])
                print(f"Mã chuyến bay: {fl['flight_id']} | Hành trình: {fl['status']} | Khởi hành: {fl['depart_time']} | Số khách: {fl['passengers']} | Số khoang: {sections} khoang.")

        # CHỨC NĂNG 2: TIẾP NHẬN CHUYẾN BAY MỚI
        elif choice == "2":
            print("\n----- TIẾP NHẬN CHUYẾN BAY MỚI -----")
            # Bẫy lỗi 1: Mã chuyến bay không được để trống
            while True:
                f_id = input("Nhập mã chuyến bay: ").strip().upper()
                if f_id:
                    break
                print("Lỗi: Mã chuyến bay không được bỏ trống!")

            # Nhập số lượng hành khách với bẫy lỗi nhập chữ (ValueError)
            while True:
                try:
                    p_count = int(input("Nhập số lượng hành khách: "))
                    if p_count >= 0:
                        break
                    print("Số lượng hành khách không được là số âm!")
                except ValueError:
                    print("Lỗi: Vui lòng nhập số lượng hành khách là một số nguyên!")

            # Bẫy lỗi 2: Nhập sai định dạng ngày tháng
            while True:
                dep_t = input("Nhập thời gian khởi hành (YYYY-MM-DD HH:MM:SS): ").strip()
                try:
                    # Thử nghiệm kiểm tra định dạng
                    datetime.strptime(dep_t, "%Y-%m-%d %H:%M:%S")
                    break
                except ValueError:
                    print("Lỗi định dạng ngày tháng! Vui lòng nhập đúng chuẩn cấu trúc YYYY-MM-DD HH:MM:SS.")

            # Nhập thời gian bay
            while True:
                try:
                    duration = int(input("Nhập thời gian bay (phút): "))
                    if duration > 0:
                        break
                    print("Thời gian bay phải lớn hơn 0 phút!")
                except ValueError:
                    print("Vui lòng nhập số phút bay hợp lệ.")

            status_route = input("Nhập chặng bay (Ví dụ: Hà Nội - Đà Nẵng): ").strip()

            # Gọi hàm đóng gói lưu trữ
            add_new_flight(flights, f_id, p_count, dep_t, duration, status_route)
            print(f"🎉 Tiếp nhận thành công chuyến bay {f_id}!")

        # CHỨC NĂNG 3: TÍNH TOÁN GIỜ HẠ CÁNH DỰ KIẾN (ETA)
        elif choice == "3":
            print("\n----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")
            search_id = input("Nhập mã chuyến bay cần tính toán ETA: ").strip().upper()
            
            try:
                target_flight = None
                for fl in flights:
                    if fl["flight_id"] == search_id:
                        target_flight = fl
                        break
                
                # Bẫy lỗi: Nếu duyệt hết danh sách mà không tìm thấy chuyến bay khớp mã
                if not target_flight:
                    raise FlightNotFoundError(f"Mã chuyến bay '{search_id}' không tồn tại trên hệ thống!")
                
                # Thực hiện tính toán thời điểm hạ cánh dự kiến
                eta_res = calculate_flight_eta(target_flight["depart_time"], target_flight["duration_min"])
                
                print(f" -> Chuyến bay {search_id} (Hành trình: {target_flight['status']})")
                print(f" -> Thời gian khởi hành thực tế: {target_flight['depart_time']}")
                print(f" -> Thời gian hạ cánh dự kiến (ETA): {eta_res.strftime('%Y-%m-%d %H:%M:%S')}")

            except FlightNotFoundError as e:
                print(f"Lỗi: {e}")

        # CHỨC NĂNG 4: KHỞI TẠO THƯ MỤC NHẬT KÝ LƯU TRỮ
        elif choice == "4":
            print("\n----- KHỞI TẠO THƯ MỤC LƯU TRỮ NHẬT KÝ -----")
            # Gọi hàm quản lý ổ đĩa an toàn
            safe_create_directory("aviation_logs")

        # CHỨC NĂNG 5: THOÁT CHƯƠNG TRÌNH
        elif choice == "5":
            print("\nCảm ơn quý khách và tổ bay đã sử dụng hệ thống! Hệ thống đang ngắt kết nối...")
            break

        # BẪY LỖI MENU: Lựa chọn nằm ngoài dải số từ 1 đến 5
        else:
            print("Lựa chọn không hợp lệ! Vui lòng thao tác nhập số từ 1 đến 5 nhé các bạn yêu.")
            show_aviation_menu()


if __name__ == "__main__":
    main()