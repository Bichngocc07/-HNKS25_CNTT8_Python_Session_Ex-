import logging
from datetime import datetime


logging.basicConfig(
    filename='tournament_app.log',
    filemode='a',
    format='[%(asctime)s] - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S,%f', 
    level=logging.INFO
)

logging.Formatter.formatTime = lambda self, record, datefmt=None: \
    datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]


matches = [
    {
        "match_id": "M01",
        "team_a": "TS",
        "team_b": "Gam",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "FL",
        "team_b": "VGM",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]


def determine_winner(match):
    """
    Xác định kết quả hoặc đội chiến thắng của một trận đấu.
    
    Args:
        match (dict): Dictionary chứa thông tin trận đấu.
        
    Returns:
        str: Tên đội thắng, "Draw" nếu hòa, hoặc "Not Started" nếu chưa diễn ra.
    """
    try:
        if "score_a" not in match or "score_b" not in match:
            raise KeyError("Dữ liệu trận đấu bị thiếu trường điểm số (score_a/score_b)!")
            
        if match["status"] == "Pending":
            return "Not Started"
            
        if match["score_a"] > match["score_b"]:
            return match["team_a"]
        elif match["score_b"] > match["score_a"]:
            return match["team_b"]
        else:
            return "Draw"
            
    except KeyError as e:
        logging.error(f"Lỗi truy xuất dữ liệu Dictionary: {e}")
        return "Error"




# CHỨC NĂNG 1: HIỂN THỊ DANH SÁCH TRẬN ĐẤU & KẾT QUẢ
def display_matches(matches_list):
    """Hiển thị bảng danh sách các trận đấu ra Console và ghi log INFO."""
    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    
    if len(matches_list) == 0:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
    else:
        print(f"{'Mã trận':<8} | {'Đội A':<8} | {'Đội B':<8} | {'Tỷ số':<6} | {'Trạng thái'}")
        print("-" * 60)
        for m in matches_list:
            try:
                m_id = m.get("match_id", "N/A")
                t_a = m.get("team_a", "N/A")
                t_b = m.get("team_b", "N/A")
                s_a = m.get("score_a", 0)
                s_b = m.get("score_b", 0)
                status = m.get("status", "N/A")
                
                print(f"{m_id:<8} | {t_a:<8} | {t_b:<8} | {s_a}:{s_b:<4} | {status}")
            except Exception as e:
                print(f"Lỗi hiển thị bản ghi trận đấu!")
                logging.error(f"Lỗi hiển thị danh sách trận đấu: {e}")
                
    logging.info("User viewed the match list.")


# CHỨC NĂNG 2: THÊM TRẬN ĐẤU MỚI
def add_match(matches_list):
    """Tiếp nhận trận đấu mới vào danh sách kèm kiểm tra các ràng buộc đầu vào."""
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")
    
    while True:
        match_id = input("Nhập mã trận đấu: ").strip().upper()
        if not match_id:
            print("Mã trận đấu không được để trống.")
            logging.warning("User tried to add a match with empty match ID.")
            continue
            
        duplicate = any(m["match_id"] == match_id for m in matches_list)
        if duplicate:
            print("Lỗi: Mã trận đấu này đã tồn tại.")
            logging.warning(f"Match ID {match_id} already exists.")
            continue
        break
        
    while True:
        team_a = input("Nhập tên đội A: ").strip()
        if not team_a:
            print("Tên đội không được để trống.")
            logging.warning("User tried to add a match with empty team name.")
            continue
        break
        
    while True:
        team_b = input("Nhập tên đội B: ").strip()
        if not team_b:
            print("Tên đội không được để trống.")
            logging.warning("User tried to add a match with empty team name.")
            continue
        break

    new_match = {
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
    matches_list.append(new_match)
    print(f"Thành công: Đã thêm trận đấu {match_id}.")
    logging.info("Match M03 added successfully")


# CHỨC NĂNG 3: CẬP NHẬT TỶ SỐ TRẬN ĐẤU
def update_match_score(matches_list):
    """Cập nhật điểm và tự động chuyển trạng thái hoàn thành kèm kiểm tra Edge Case."""
    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")
    match_id = input("Nhập mã trận đấu cần cập nhật: ").strip().upper()
    
    target_match = None
    for m in matches_list:
        if m["match_id"] == match_id:
            target_match = m
            break
            
    if not target_match:
        print("Không tìm thấy trận đấu có mã vừa nhập.")
        logging.warning(f"User tried to update non-existing match {match_id}")
        return

    print(f"Trận đấu: {target_match['team_a']} vs {target_match['team_b']} ({target_match['status']})")
    
    while True:
        try:
            score_a_input = input("Nhập điểm đội A: ").strip()
            score_a = int(score_a_input)
            if score_a < 0:
                print("Điểm số phải lớn hơn hoặc bằng 0.")
                logging.error(f"Negative score input detected: {score_a}")
                continue
            break
        except ValueError:
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.error(f"Invalid score input. Error: Invalid literal for int() with base 10: '{score_a_input}'")
            
    while True:
        try:
            score_b_input = input("Nhập điểm đội B: ").strip()
            score_b = int(score_b_input)
            if score_b < 0:
                print("Điểm số phải lớn hơn hoặc bằng 0.")
                logging.error(f"Negative score input detected: {score_b}")
                continue
            break
        except ValueError:
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.error(f"Invalid score input. Error: Invalid literal for int() with base 10: '{score_b_input}'")

    if score_a == 0 and score_b == 0:
        confirm = input("Tỷ số đang là 0-0. Trọng tài có xác nhận trận đấu đã hoàn thành không? (y/n): ").strip().lower()
        if confirm == 'y':
            target_match["status"] = "Completed"
        else:
            target_match["status"] = "Pending"
    else:
        target_match["status"] = "Completed"

    target_match["score_a"] = score_a
    target_match["score_b"] = score_b
    
    print(f"Thành công: Đã cập nhật tỷ số trận đấu {match_id}.")
    logging.info("Match M02 score updated successfully")


# CHỨC NĂNG 4: BÁO CÁO THỐNG KÊ GIẢI ĐẤU
def generate_report(matches_list):
    """Thống kê chi tiết số trận đã hoàn thành và danh sách đội thắng cuộc."""
    print("\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")
    
    completed_count = 0
    print("Các trận đấu đã hoàn thành:")
    
    for m in matches_list:
        winner = determine_winner(m)
        if m["status"] == "Completed":
            completed_count += 1
            if winner == "Draw":
                print(f"- Trận {m['match_id']}: Hòa")
            else:
                print(f"- Trận {m['match_id']}: {winner} thắng")
                
    if completed_count == 0:
        print("Chưa có trận đấu nào hoàn thành.")
        
    print(f"Tổng số trận đã hoàn thành: {completed_count}")
    logging.info("User generated tournament report.")


# =============================================================================
# 5. VÒNG LẶP MENU ĐIỀU KHIỂN CHÍNH
# =============================================================================
def main():
    while True:
        print("\n===== Hệ thống quản lý giải đấu RIKKEI ESPORTS =====")
        print("1. Xem lịch thi đấu & kết quả")
        print("2. Thêm trận đấu mới")
        print("3. Cập nhật tỷ số trận đấu")
        print("4. Báo cáo thống kê")
        print("5. Thoát chương trình")
        print("----------------------------------------------------")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            display_matches(matches)
        elif choice == "2":
            add_match(matches)
        elif choice == "3":
            update_match_score(matches)
        elif choice == "4":
            generate_report(matches)
        elif choice == "5":
            print("Đóng hệ thống quản lý giải đấu thành công. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 5.")
            logging.warning("Invalid menu choice selected.")

if __name__ == "__main__":
    main()
