
data = [
    ("Levi", 120, 2500),        
    ("SofM", 150),               
    ("Optimus", 100, "N/A")      
]


def calculate_bonus(matches, mmr):
    """
    Hàm nhận vào số trận đấu và điểm mmr, xử lý ép kiểu và tính toán điểm thưởng.
    Công thức: Bonus RP = (Số trận đã chơi * 10) + (Điểm MMR * 0.5)
    """
    int_matches = int(matches)
    float_mmr = float(mmr)
    
    bonus_value = (int_matches * 10) + (float_mmr * 0.5)
    return bonus_value



def process(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    
    for player in player_records:
        try:
            
            name = player[0]
            matches = player[1]
            
            mmr = player[2]
            
            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus} RP")
            
        except IndexError:
            
            print(f"Lỗi - Hồ sơ thiếu thông tin")
            continue  
            
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ")
            continue 
    print("--- HOÀN TẤT ---")



if __name__ == "__main__":
    process(data)
