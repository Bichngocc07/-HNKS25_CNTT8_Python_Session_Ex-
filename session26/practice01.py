# =============================================================================
# HỆ THỐNG CHIẾN ĐẤU NHÂN VẬT GAME - RIKKEI STUDIOS (OOP CORE)
# =============================================================================

class Character:
    """Lớp cha nền tảng quản lý các thông số cơ bản của mọi nhân vật trong game."""
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power


class Warrior(Character):
    """Lớp con Chiến binh - Kế thừa toàn bộ sức mạnh từ Character và bổ sung Giáp."""
    def __init__(self, name, hp, attack_power, bonus_armor):
        # YÊU CẦU 1: Sử dụng super() để kế thừa chính xác các thuộc tính cơ bản từ lớp cha
        super().__init__(name, hp, attack_power)
        # Bổ sung thuộc tính riêng biệt của hệ lớp Chiến binh
        self.bonus_armor = bonus_armor

    def get_total_power(self):
        """Tính toán tổng sức mạnh chiến đấu thực tế dựa trên Tấn công và Giáp."""
        return self.attack_power + self.bonus_armor

    # -------------------------------------------------------------------------
    # KỸ THUẬT NẠP CHỒNG TOÁN TỬ (OPERATOR OVERLOADING)
    # -------------------------------------------------------------------------
    def __gt__(self, other):
        """
        Dunder method __gt__ (Greater Than) tái định nghĩa toán tử '>'.
        Giúp hệ thống tự động so sánh sức mạnh tổng giữa 2 chiến binh.
        """
        # Kiểm tra phòng hờ nếu đối tượng đem so sánh không cùng thuộc lớp Warrior
        if not isinstance(other, Warrior):
            return NotImplemented
            
        # Luật game: Chiến binh nào có tổng sức mạnh lớn hơn thì thắng
        return self.get_total_power() > other.get_total_power()


# =============================================================================
# KỊCH BẢN CHẠY TRẬN ĐẤU ĐIỀU PHỐI (MATCHMAKING)
# =============================================================================
def main():
    print("====== KÍCH HOẠT HỆ THỐNG TRẬN ĐẤU RIKKEI STUDIOS ======\n")

    # 1. Khởi tạo 2 tượng đài chiến binh
    # w1: Arthur -> Sức mạnh tổng: 150 (Tấn công) + 50 (Giáp) = 200
    w1 = Warrior("Arthur", 1000, 150, 50)
    
    # w2: Lancelot -> Sức mạnh tổng: 180 (Tấn công) + 10 (Giáp) = 190
    w2 = Warrior("Lancelot", 800, 180, 10)

    # 2. In thông báo xuất trận (Đã sửa lỗi AttributeError thành công)
    print(f"Chiến binh {w1.name} xuất trận!")
    print(f"Chiến binh {w2.name} xuất trận!")
    print("-" * 54)

    # 3. Thực hiện thuật toán Matchmaking so sánh sức mạnh bằng toán tử '>' trực tiếp
    # Nhờ hàm __gt__, dòng lệnh này sẽ tự động gọi w1.get_total_power() > w2.get_total_power()
    if w1 > w2:
        print(f"🔥 Kết quả: {w1.name} mạnh hơn {w2.name}!")
    else:
        print(f"🔥 Kết quả: {w2.name} mạnh hơn hoặc bằng {w1.name}!")
        
    print("\n========================================================")


if __name__ == "__main__":
    main()