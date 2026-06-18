# =============================================================================
# 1. DỮ LIỆU ĐẦU VÀO (Dữ liệu gốc trích xuất từ API của game dưới dạng chuỗi)
# =============================================================================
players_data = [
    ("Taker", "10", "2", "8"),          # Tuyển thủ 1: Dữ liệu hoàn toàn bình thường
    ("ShowMaker", "15", "0", "10"),     # Tuyển thủ 2: Không chết mạng nào (Deaths = 0) -> Gây lỗi ZeroDivisionError
    ("Chovy", "12", "ba", "5")          # Tuyển thủ 3: Lỗi dữ liệu chữ "ba" -> Gây lỗi ValueError
]


# =============================================================================
# 2. MODULAR (Tách hàm tính toán KDA độc lập theo nguyên tắc DRY)
# =============================================================================
def calculate_kda(kills, deaths, assists):
    """
    Hàm xử lý logic tính toán chỉ số KDA từ các tham số dạng chuỗi.
    Ép kiểu dữ liệu và bẫy lỗi cục bộ tại đây.
    """
    # Ép kiểu dữ liệu từ chuỗi (String) sang số nguyên (Integer)
    int_kills = int(kills)
    int_deaths = int(deaths)
    int_assists = int(assists)
    
    # Xử lý trường hợp hoàn hảo: Tuyển thủ không bị hạ gục mạng nào (Deaths == 0)
    if int_deaths == 0:
        # Sử dụng cơ chế quăng lỗi chủ động hoặc trả về một tín hiệu chuỗi đặc biệt
        raise ZeroDivisionError
        
    # Áp dụng công thức chuẩn và làm tròn kết quả đến 2 chữ số thập phân
    kda_value = round((int_kills + int_assists) / int_deaths, 2)
    return kda_value


# =============================================================================
# 3. HÀM CHÍNH ĐIỀU KHIỂN HỆ THỐNG XẾP HẠNG
# =============================================================================
def display_kda_leaderboard(players_list):
    """
    Hàm duyệt danh sách toàn bộ các tuyển thủ, gọi hàm xử lý tính toán KDA
    và thực hiện bẫy lỗi Exception Handling bằng khối Try-Except.
    """
    print("--- BẢNG XẾP HẠNG KDA ---")
    
    # Sử dụng tên biến Clean Code rõ nghĩa thay thế cho x, n, k, d, a
    for player_stats in players_list:
        player_name = player_stats[0]
        kills_str = player_stats[1]
        deaths_str = player_stats[2]
        assists_str = player_stats[3]
        
        # Bắt đầu khối kiểm soát và bẫy lỗi dữ liệu
        try:
            # Gọi hàm mô-đun để thực hiện tính toán
            kda = calculate_kda(kills_str, deaths_str, assists_str)
            print(f"Tuyển thủ {player_name} có chỉ số KDA là: {kda}")
            
        except ZeroDivisionError:
            # Xử lý lỗi chia cho 0: Tuyển thủ có trận đấu hoàn hảo (Perfect Game)
            print(f"Tuyển thủ {player_name}: KDA Hoàn hảo (Perfect Game)!")
            # Từ khóa continue giúp chương trình không bị sập, nhảy sang tuyển thủ kế tiếp
            continue 
            
        except ValueError:
            # Xử lý lỗi ép kiểu dữ liệu: Dữ liệu API trả về bị sai định dạng chữ/số
            print(f"Tuyển thủ {player_name}: Lỗi dữ liệu không hợp lệ!")
            # Tiếp tục bỏ qua phần tử lỗi để tính toán cho người phía sau
            continue

    print("--- HOÀN TẤT ---")

# =============================================================================
# 4. KHỞI CHẠY HỆ THỐNG
# =============================================================================
if __name__ == "__main__":
    display_kda_leaderboard(players_data)