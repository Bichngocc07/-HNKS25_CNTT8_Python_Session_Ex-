
players_data = [
    ("Taker", "10", "2", "8"),         
    ("ShowMaker", "15", "0", "10"),     
    ("Chovy", "12", "ba", "5")       
]



def calculate_kda(kills, deaths, assists):
    """
    Hàm xử lý logic tính toán chỉ số KDA từ các tham số dạng chuỗi.
    Ép kiểu dữ liệu và bẫy lỗi cục bộ tại đây.
    """
   
    int_kills = int(kills)
    int_deaths = int(deaths)
    int_assists = int(assists)
    
    if int_deaths == 0:
        raise ZeroDivisionError
        
    kda_value = round((int_kills + int_assists) / int_deaths, 2)
    return kda_value



def display_kda_leaderboard(players_list):
    """
    Hàm duyệt danh sách toàn bộ các tuyển thủ, gọi hàm xử lý tính toán KDA
    và thực hiện bẫy lỗi Exception Handling bằng khối Try-Except.
    """
    print("--- BẢNG XẾP HẠNG KDA ---")
    
    for player_stats in players_list:
        player_name = player_stats[0]
        kills_str = player_stats[1]
        deaths_str = player_stats[2]
        assists_str = player_stats[3]
        
        try:
            kda = calculate_kda(kills_str, deaths_str, assists_str)
            print(f"Tuyển thủ {player_name} có chỉ số KDA là: {kda}")
            
        except ZeroDivisionError:
            print(f"Tuyển thủ {player_name}: KDA Hoàn hảo (Perfect Game)!")
            continue 
            
        except ValueError:
            print(f"Tuyển thủ {player_name}: Lỗi dữ liệu không hợp lệ!")
            continue

    print("--- HOÀN TẤT ---")


if __name__ == "__main__":
    display_kda_leaderboard(players_data)
