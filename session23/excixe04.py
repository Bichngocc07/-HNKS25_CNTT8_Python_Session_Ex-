import os
import random
import string
from datetime import datetime

import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# =============================================================================
# DỮ LIỆU BAN ĐẦU (Lưu trữ trong file dưới dạng List chứa các Dictionary)
# =============================================================================
student_records = [
    {
        "student_id": "SV001",
        "name": "  nguyen  van  a  ",
        "scores": [8.5, 7.0, 9.0]
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "scores": [6.0, "abc", 7.0]  
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "scores": [4.0, 5.0, 3.5]
    }
]


# =============================================================================
# ĐỊNH NGHĨA CÁC HÀM CHỨC NĂNG NGHIỆP VỤ
# =============================================================================

def calculate_average(scores):
    """Tính điểm trung bình của một danh sách điểm, bỏ qua các giá trị lỗi."""
    valid_scores = []
    for s in scores:
        try:
            valid_scores.append(float(s))
        except ValueError:
            continue
            
    if not valid_scores:
        return 0.0
        
    return round(sum(valid_scores) / len(valid_scores), 2)


def classify_student(average):
    """Phân loại học lực dựa trên điểm trung bình của sinh viên."""
    if average >= 8.0:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"


# --- Chức năng 1: Xem danh sách sinh viên và điểm trung bình ---
def display_student_scores(records):
    print("\n--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    for r in records:
        dtb = calculate_average(r["scores"])
        rank = classify_student(dtb)
        
        scores_str = ", ".join(str(s) for s in r["scores"])
        print(f"[{r['student_id']}] {r['name']} | Điểm: [{scores_str}] | ĐTB: {dtb:.2f} - {rank}")
    print("-" * 50)


# --- Chức năng 2: Chuẩn hóa tên sinh viên ---
def normalize_student_names(records):
    print("\n--- CHUẨN HÓA TÊN SINH VIÊN ---")
    for r in records:
        words = r["name"].strip().split()
        r["name"] = " ".join(words).title()
        print(f"Đã chuẩn hóa: {r['name']}")
    print("Số liệu chuẩn hóa toàn bộ học sinh viên thành công.")


# --- Chức năng 3: Sinh mã bài tập ngẫu nhiên ---
def generate_assignment_code():
    print("\n--- SINH MÃ BÀI TẬP ---")
    pool = string.ascii_uppercase + string.digits
    random_chars = "".join(random.choice(pool) for _ in range(4))
    
    code = f"PY-{random_chars}"
    print(f"Mã bài tập của học phần là: {code}")
    return code


# --- Chức năng 4: Xuất báo cáo học tập ---
def export_learning_report(records):
    print("\n--- XUẤT BÁO CÁO HỌC TẬP ---")
    
    total_students = len(records)
    passed_count = 0
    failed_count = 0
    
    for r in records:
        dtb = calculate_average(r["scores"])
        if dtb >= 5.0:
            passed_count += 1
        else:
            failed_count += 1
            
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    filename = "learning_report.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("======= BÁO CÁO HỌC TẬP RIKKEI ACADEMY =======\n")
            f.write(f"Thời gian xuất bản: {current_time}\n")
            f.write("----------------------------------------------\n")
            f.write(f"Tổng số sinh viên: {total_students}\n")
            f.write(f"Số sinh viên đạt yêu cầu (ĐTB >= 5.0): {passed_count}\n")
            f.write(f"Số sinh viên cần cải thiện (ĐTB < 5.0): {failed_count}\n")
            f.write("==============================================\n")
            
        print(Fore.GREEN + f"Tạo file thành công!")
        print(f"Sơ đồ xuất báo cáo ra file: {filename}")
        
    except Exception as e:
        print(Fore.RED + f"Đã xảy ra lỗi khi ghi file: {e}")


# =============================================================================
# VÒNG LẶP ĐIỀU KHIỂN MENU TRUNG TÂM (HÀM MAIN)
# =============================================================================
def main():
    while True:
        print("\n----- HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY -----")
        print("1. Xem danh sách sinh viên và điểm trung bình")
        print("2. Chuẩn hóa tên sinh viên")
        print("3. Sinh mã bài tập ngẫu nhiên")
        print("4. Xuất báo cáo học tập")
        print("5. Thoát chương trình")
        print("----------------------------------------------------")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            display_student_scores(student_records)
        elif choice == "2":
            normalize_student_names(student_records)
        elif choice == "3":
            generate_assignment_code()
        elif choice == "4":
            export_learning_report(student_records)
        elif choice == "5":
            print(Fore.CYAN + "Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print(Fore.YELLOW + "Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main()
