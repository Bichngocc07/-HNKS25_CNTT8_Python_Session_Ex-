# =============================================================================
# 1. DANH SÁCH DỮ LIỆU ĐẦU VÀO (Dirty Data từ API)
# =============================================================================
data = [
    ("Levi", 120, 2500),         # Dữ liệu chuẩn
    ("SofM", 150),               # Lỗi API: Bị thiếu mất trường MMR (Tuple chỉ có 2 phần tử)
    ("Optimus", 100, "N/A")      # Lỗi dữ liệu: Điểm MMR bị ghi chữ "N/A"
]


# =============================================================================
# 2. MODULAR (Tách hàm tính toán điểm thưởng cuối mùa - Đảm bảo DRY)
# =============================================================================
def calculate_bonus(matches, mmr):
    """
    Hàm nhận vào số trận đấu và điểm mmr, xử lý ép kiểu và tính toán điểm thưởng.
    Công thức: Bonus RP = (Số trận đã chơi * 10) + (Điểm MMR * 0.5)
    """
    # Ép kiểu dữ liệu về số thực/số nguyên để tính toán
    int_matches = int(matches)
    float_mmr = float(mmr)
    
    # Tính toán kết quả
    bonus_value = (int_matches * 10) + (float_mmr * 0.5)
    return bonus_value


# =============================================================================
# 3. HÀM XỬ LÝ CHÍNH VÀ BẪY LỖI (EXCEPTION HANDLING)
# =============================================================================
def process(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    
    # Duyệt danh sách hồ sơ tuyển thủ
    for player in player_records:
        try:
            # Bẫy lỗi IndexError: Kiểm tra thủ công độ dài hoặc dùng try-except
            # Trích xuất thông tin cơ bản
            name = player[0]
            matches = player[1]
            
            # Cố tình lấy phần tử thứ 3, nếu thiếu trường sẽ quăng ra IndexError
            mmr = player[2]
            
            # Gọi hàm tính toán điểm thưởng
            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus} RP")
            
        except IndexError:
            # Xử lý khi bộ Tuple bị thiếu mất trường dữ liệu (ví dụ trường hợp của SofM)
            # Vì thiếu dữ liệu nên không thể lấy player[0] một cách an toàn nếu tuple rỗng,
            # nhưng ở đây biết chắc phần tử đầu là Tên: player[0]
            print(f"Lỗi - Hồ sơ thiếu thông tin")
            continue  # Bỏ qua và chạy tiếp các tuyển thủ phía sau
            
        except ValueError:
            # Xử lý khi điểm MMR không thể ép sang kiểu số (ví dụ trường hợp "N/A" của Optimus)
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ")
            continue  # Bỏ qua và chạy tiếp các tuyển thủ phía sau

    print("--- HOÀN TẤT ---")


# =============================================================================
# 4. CHẠY HỆ THỐNG
# =============================================================================
if __name__ == "__main__":
    process(data)