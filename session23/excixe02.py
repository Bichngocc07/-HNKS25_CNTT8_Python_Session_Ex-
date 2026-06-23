import os
import math
from datetime import datetime

# =============================================================================
# 1. KHỞI TẠO DANH SÁCH DỮ LIỆU ĐẦU VÀO (Mô phỏng dữ liệu thô từ API)
# =============================================================================
raw_files = [
    ("video_pos_01.mp4", "4194304", "120", "2026-06-23"),
    ("media_trailer.mp4", "16777216", "145", "2026-06-31"),
    ("clip_short.mp4", "8388608", "15", "2026-06-15")
]

# =============================================================================
# 2. ĐỊNH NGHĨA CÁC HÀM CHỨC NĂNG (Kiến trúc gói xử lý độc lập)
# =============================================================================

def calculate_disk_blocks(size_bytes, block_size=4096):
    """
    Tính toán số lượng khối phân vùng (Disk Blocks) cần thiết để lưu trữ tệp.
    Áp dụng thuật toán làm tròn lên (Ceiling) tránh mất mát dữ liệu phần cứng.
    """
    bytes_val = int(size_bytes)
    blocks = math.ceil(bytes_val / block_size)
    return bytes_val, blocks


def safe_create_dir(dir_path):
    """
    Tạo thư mục lưu trữ phân cấp một cách an toàn.
    Sử dụng exist_ok=True để phòng ngừa lỗi FileExistsError nếu thư mục đã có sẵn.
    """
    os.makedirs(dir_path, exist_ok=True)


# --- Thuộc Package analytics ---
def parse_and_inspect_date(date_str):
    """
    Chuyển đổi chuỗi ngày tháng sang đối tượng datetime để kiểm tra tính hợp lệ.
    Bẫy ngoại lệ ValueError nếu chuỗi thời gian bị sai quy định cấu trúc thực tế.
    """
    valid_date = datetime.strptime(date_str, "%Y-%m-%d")
    return valid_date


# =============================================================================
# 3. HÀM CHẠY CHÍNH ĐIỀU KHIỂN LUỒNG HỆ THỐNG
# =============================================================================
def main():
    print("========= HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA =========")
    print("[SYSTEM] Tiến hành rà soát dữ liệu tệp tin gốc... BẮT ĐẦU.")
    print("----------------------------------------------------------------")
    
    success_count = 0
    total_count = len(raw_files)
    
    for file_record in raw_files:
        file_name = file_record[0]
        size_bytes_str = file_record[1]
        duration_str = file_record[2]
        upload_date_str = file_record[3]
        
        try:
            inspected_date = parse_and_inspect_date(upload_date_str)
            
            actual_size, total_blocks = calculate_disk_blocks(size_bytes_str)
            
        
            if file_name.lower().endswith(('.mp4', '.mkv', '.avi')):
                sub_folder = "video"
            elif file_name.lower().endswith(('.mp3', '.wav', '.flac')):
                sub_folder = "audio"
            else:
                sub_folder = "other"
                
            destination_path = os.path.join("media_root", sub_folder)
            
            safe_create_dir(destination_path)
            
            print(f"[TỆP TIN: {file_name}]")
            print(f" + Dung lượng thực tế: {actual_size:,} bytes")
            print(f" + Số khối phân vùng ({total_blocks} blocks) -> ĐẠT CHUẨN.")
            print(f" + Trạng thái phân loại:  Đã lưu vào thư mục '{destination_path}'")
            success_count += 1
            
        except ValueError:
            print(f"[TỆP TIN: {file_name}]")
            print(f" + Trạng thái phân loại: Thất bại (Lỗi định dạng ngày upload '{upload_date_str}' không tồn tại!)")
            
        print("-" * 64)
        
    print(f"TIẾN ĐỘ DUYỆT: Hoàn thành xử lý {success_count}/{total_count} tập tin thành công. Hệ thống ổn định.")


if __name__ == "__main__":
    main()
