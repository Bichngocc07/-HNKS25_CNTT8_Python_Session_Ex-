import os
from abc import ABC, abstractmethod

# =============================================================================
# 1. LỚP CHA TRỪU TƯỢNG (ABSTRACT BASE CLASS)
# =============================================================================
class Champion(ABC):
    """Lớp trừu tượng Champion làm nền tảng cho toàn bộ quân cờ trong game."""
    
    def __init__(self, champion_id, name, hp, atk):
        self.champion_id = champion_id
        self.name = name
        self.hp = hp
        self.atk = atk

    @abstractmethod
    def calculate_skill_damage(self):
        """Phương thức trừu tượng bắt buộc các hệ tướng con phải tự định nghĩa."""
        pass

    def get_combat_power(self):
        """Tính điểm chiến lực tổng hợp của quân cờ."""
        # Công thức: Máu * 0.5 + Sát thương kỹ năng * 1.5
        skill_dmg = self.calculate_skill_damage()
        return round(self.hp * 0.5 + skill_dmg * 1.5, 1)

    # -------------------------------------------------------------------------
    # NẠP CHỒNG TOÁN TỬ (OPERATOR OVERLOADING)
    # -------------------------------------------------------------------------
    def __add__(self, other):
        """Toán tử '+': Cộng dồn điểm chiến lực của các quân cờ hoặc với một số số thực."""
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __radd__(self, other):
        """Hỗ trợ toán tử cộng dồn tích lũy khi dùng hàm sum()."""
        if other == 0:
            return self.get_combat_power()
        return self + other

    def __gt__(self, other):
        """Toán tử '>': So sánh quân cờ nào có điểm chiến lực cao hơn."""
        if not isinstance(other, Champion):
            return NotImplemented
        return self.get_combat_power() > other.get_combat_power()


# =============================================================================
# 2. CÁC LỚP CON CỤ THỂ (CONCRETE CLASSES)
# =============================================================================

class Warrior(Champion):
    """Hệ lớp Chiến binh - Thiên về chống chịu và cận chiến."""
    
    def __init__(self, champion_id, name, hp, atk, shield_bonus):
        super().__init__(champion_id, name, hp, atk)
        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        # Công thức: Sát thương = atk * 2 + shield_bonus
        return self.atk * 2 + self.shield_bonus


class Mage(Hero if 'Hero' in globals() else Champion): # Kế thừa an toàn từ Champion
    """Hệ lớp Pháp sư - Thiên về sát thương phép diện rộng."""
    
    def __init__(self, champion_id, name, hp, atk, ability_power):
        super().__init__(champion_id, name, hp, atk)
        self.ability_power = ability_power

    def calculate_skill_damage(self):
        # Công thức: Sát thương = atk * 3 * ability_power
        return round(self.atk * 3 * self.ability_power, 1)


# =============================================================================
# 3. VÒNG LẶP ĐIỀU KHIỂN CHƯƠNG TRÌNH CHÍNH (MENU)
# =============================================================================
def main():
    # Khởi tạo kho dữ liệu tướng mặc định ban đầu theo yêu cầu nghiệp vụ
    champion_pool = {
        "WAR01": Warrior("WAR01", "Rikkei Knight", 1200, 150, 100),
        "WAR02": Warrior("WAR02", "Steel Guardian", 1400, 130, 150),
        "MAG01": Mage("MAG01", "Rikkei Wizard", 800, 180, 2.0)
    }

    while True:
        print("\n====== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH AUTO-BATTLER ======")
        print("1. Hiển thị thông tin tướng hiện có")
        print("2. Thêm quân cờ mới")
        print("3. So sánh 2 quân cờ")
        print("4. Tính tổng chiến lực Đội Hình Ra Trận")
        print("5. Thoát chương trình")
        print("----------------------------------------------------")
        
        choice = input("Chọn chức năng (1-5): ").strip()

        # CHỨC NĂNG 1: HIỂN THỊ THÔNG TIN TƯỚNG HIỆN CÓ
        if choice == "1":
            print("\n--- DANH SÁCH CÁC TƯỚNG HIỆN CÓ ---")
            print(f"{'Mã':<6} | {'Tên tướng':<16} | {'Hệ':<8} | {'HP':<6} | {'ATK':<5} | {'Chiến lực'}")
            print("-" * 65)
            for c_id, champ in champion_pool.items():
                class_name = "Warrior" if isinstance(champ, Warrior) else "Mage"
                print(f"{c_id:<6} | {champ.name:<16} | {class_name:<8} | {champ.hp:<6} | {champ.atk:<5} | {champ.get_combat_power():,}")

        # CHỨC NĂNG 2: THÊM QUÂN CỜ MỚI
        elif choice == "2":
            print("\n--- THÊM QUÂN CỜ MỚI ---")
            # Bẫy lỗi 3: Kiểm tra trùng lặp mã tướng
            c_id = input("Nhập mã tướng (ID): ").strip().upper()
            if c_id in champion_pool:
                print(f"❌ Lỗi: Mã tướng '{c_id}' đã tồn tại trong hệ thống pool!")
                continue

            print("Chọn hệ tướng: 1 - Warrior | 2 - Mage")
            type_choice = input("Lựa chọn (1-2): ").strip()
            if type_choice not in ["1", "2"]:
                print("❌ Lựa chọn hệ tướng không hợp lệ!")
                continue

            name = input("Nhập tên tướng: ").strip()
            if not name:
                print("❌ Tên tướng không được để trống!")
                continue

            try:
                hp = int(input("Nhập HP: "))
                atk = int(input("Nhập ATK: "))
                if hp <= 0 or atk <= 0:
                    print("❌ Chỉ số HP và ATK phải lớn hơn 0!")
                    continue

                if type_choice == "1":
                    shield = int(input("Nhập chỉ số Giáp cộng thêm (Shield): "))
                    if shield < 0:
                        print("❌ Chỉ số Giáp không được âm!")
                        continue
                    new_champ = Warrior(c_id, name, hp, atk, shield)
                else:
                    ap = float(input("Nhập hệ số Khuyếch đại phép (AP): "))
                    if ap <= 0:
                        print("❌ Hệ số AP phải lớn hơn 0!")
                        continue
                    new_champ = Mage(c_id, name, hp, atk, ap)

                # Lưu vào database pool
                champion_pool[c_id] = new_champ
                print(f"🎉 Thêm tướng {name} thành công!")

            except ValueError:
                print("❌ Lỗi: Định dạng chữ số nhập vào không hợp lệ!")

        # CHỨC NĂNG 3: SO SÁNH 2 QUÂN CỜ
        elif choice == "3":
            print("\n--- SO SÁNH SỨC MẠNH TƯỚNG ---")
            id1 = input("Nhập mã tướng thứ nhất: ").strip().upper()
            id2 = input("Nhập mã tướng thứ hai: ").strip().upper()

            if id1 not in champion_pool or id2 not in champion_pool:
                print("❌ Lỗi: Một hoặc cả hai mã tướng nhập vào không tồn tại!")
                continue

            champ1 = champion_pool[id1]
            champ2 = champion_pool[id2]

            print(f"\nThông tin so sánh:")
            print(f" + [{id1}] {champ1.name} - Chiến lực: {champ1.get_combat_power()}")
            print(f" + [{id2}] {champ2.name} - Chiến lực: {champ2.get_combat_power()}")

            # Ứng dụng nạp chồng toán tử '>' trực tiếp giữa 2 object
            if champ1 > champ2:
                print(f"➔ Kết quả: [{id1}] {champ1.name} MẠNH HƠN [{id2}] {champ2.name}")
            elif champ2 > champ1:
                print(f"➔ Kết quả: [{id2}] {champ2.name} MẠNH HƠN [{id1}] {champ1.name}")
            else:
                print(f"➔ Kết quả: Hai quân cờ có sức mạnh chiến lực ngang nhau!")

        # CHỨC NĂNG 4: TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH RA TRẬN
        elif choice == "4":
            print("\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH ---")
            lineup_input = input("Nhập danh sách mã tướng ra trận (phân tách bằng dấu phẩy, ví dụ: WAR01,MAG01): ")
            
            # Tách chuỗi thành list các mã tướng
            id_list = [i.strip().upper() for i in lineup_input.split(",") if i.strip()]
            
            battle_lineup = []
            has_error = False
            
            for c_id in id_list:
                if c_id in champion_pool:
                    battle_lineup.append(champion_pool[c_id])
                else:
                    print(f"❌ Lỗi: Mã tướng '{c_id}' không tồn tại trong kho lưu trữ!")
                    has_error = True
                    break
            
            if has_error or not battle_lineup:
                continue

            print("\nDanh sách đội hình ra trận:")
            for idx, champ in enumerate(battle_lineup, 1):
                print(f" {idx}. {champ.name} | Chiến lực: {champ.get_combat_power()}")
            
            # Sử dụng toán tử '+' đã được nạp chồng thông qua cơ chế tính tổng của hàm sum()
            total_power = sum(battle_lineup)
            print(f"➔ Tổng chiến lực đội hình: {total_power:,}")

        # CHỨC NĂNG 5: THOÁT CHƯƠNG TRÌNH
        elif choice == "5":
            print("\nCảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main()