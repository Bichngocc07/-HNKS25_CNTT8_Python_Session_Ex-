from abc import ABC, abstractmethod

# =============================================================================
# 1. ĐỊNH NGHĨA KHUÔN MẪU LỚP CHA TRỪU TƯỢNG (ABSTRACT BASE CLASS)
# =============================================================================
class Hero(ABC):
    """Lớp cha trừu tượng làm khuôn mẫu nghiêm ngặt cho mọi vị tướng trong game."""
    
    @abstractmethod
    def use_ultimate(self):
        """Phương thức trừu tượng buộc toàn bộ lớp con phải override hành vi kỹ năng."""
        pass


# =============================================================================
# 2. XÂY DỰNG CÁC LỚP CON CHI TIẾT (CONCRETE CLASSES)
# =============================================================================

class Mage(Hero):
    """Lớp Pháp Sư - Kế thừa từ Hero."""
    def use_ultimate(self):
        print(" Pháp Sư tung chiêu: MƯA SAO BẰNG!")


class Assassin(Hero):
    """Lớp Sát Thủ - Kế thừa từ Hero và sửa lỗi đặt sai tên hàm stealth_kill()."""
    def use_ultimate(self):
        print(" Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")


# =============================================================================
# 3. KỊCH BẢN KHỞI CHẠY TRẬN ĐẤU (RUNTIME CONTROLLER)
# =============================================================================
def main():
    print("--- LOADING TRẬN ĐẤU ---")
    
    try:
       
        team_heroes = [Mage(), Assassin()]
        print("Tải trận đấu thành công! Các tướng đã sẵn sàng...\n")
        
    except TypeError as e:
        print(f"[HỆ THỐNG PHÁT HIỆN LỖI SỚM]: {e}")
        return

    print("--- GIAO TRANH TỔNG BẮT ĐẦU ---")
    
    for hero in team_heroes:
        hero.use_ultimate()
        
    print("\n------------------------------------------------")


if __name__ == "__main__":
    main()
