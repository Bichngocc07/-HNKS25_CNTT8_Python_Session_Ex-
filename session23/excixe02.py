import os
import math
from datetime import datetime

# =============================================================================
# 1. KHỞI TẠO DANH SÁCH DỮ LIỆU ĐẦU VÀO (Mô phỏng dữ liệu thô từ API)
# =============================================================================
raw_files = [
    # Bản ghi 1: Dữ liệu hoàn toàn chuẩn chỉnh
    ("video_pos_01.mp4", "4194304", "120", "2026-06-23"),
    # Bản ghi 2: Lỗi định dạng ngày tháng (Tháng 6 chỉ có 30 ngày) -> ValueError
    ("media_trailer.mp4", "16777216", "145", "2026-06-31"),
    # Bản ghi 3: Dữ liệu hoàn toàn chuẩn chỉnh
    ("clip_short.mp4", "8388608", "15", "2026-06-15")
]

# =============================================================================
# 2. ĐỊNH NGHĨA CÁC HÀM CHỨC NĂNG (Kiến trúc gói xử lý độc lập)
# =============================================================================

# --- Thuộc Package storage ---
def calculate_disk_blocks(size_bytes, block_size=4096):
    """
    Tính toán số lượng khối phân vùng (Disk Blocks) cần thiết để lưu trữ tệp.
    Áp dụng thuật toán làm tròn lên (Ceiling) tránh mất mát dữ liệu phần cứng.
    """
    bytes_val = int(size_bytes)
    # Công thức làm tròn lên: chia phần nguyên và cộng 1 nếu có dư
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
    # Ép kiểu dữ liệu nghiêm ngặt theo định dạng Năm-Tháng-Ngày mẫu
    valid_date = datetime.strptime(date_str, "%Y-%m-%d")
    return valid_date


# =============================================================================
# 3. HÀM CHẠY CHÍNH ĐIỀU KHIỂN LUỒNG HỆ THỐNG
# =============================================================================
def main():
    print("========= HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA =========")
    print("[SYSTEM] Tiến hành rà soát dữ liệu tệp tin gốc... BẮT ĐẦU.")
    print("----------------------------------------------------------------")
    
    # Khởi tạo các biến bộ đếm để báo cáo tiến độ cuối cùng
    success_count = 0
    total_count = len(raw_files)
    
    # Duyệt qua từng bản ghi dữ liệu tệp thô trong danh sách
    for file_record in raw_files:
        file_name = file_record[0]
        size_bytes_str = file_record[1]
        duration_str = file_record[2]
        upload_date_str = file_record[3]
        
        # Bắt đầu chặng bẫy lỗi xử lý dữ liệu (Exception Handling)
        try:
            # 1. Thẩm định và phân tích ngày tháng upload tệp tin trước
            inspected_date = parse_and_inspect_date(upload_date_str)
            
            # 2. Nếu ngày tháng hợp lệ, tiến hành tính toán dung lượng phân vùng khối ổ đĩa
            actual_size, total_blocks = calculate_disk_blocks(size_bytes_str)
            
            # 3. Phân loại định dạng tệp tin dựa trên phần đuôi mở rộng để chọn thư mục lưu trữ
            # .lower() để phòng hờ trường hợp người dùng gõ đuôi IN HOA (.MP4)
            if file_name.lower().endswith(('.mp4', '.mkv', '.avi')):
                sub_folder = "video"
            elif file_name.lower().endswith(('.mp3', '.wav', '.flac')):
                sub_folder = "audio"
            else:
                sub_folder = "other"
                
            # Tạo đường dẫn lưu trữ cấu trúc Production theo mẫu: media_root/tên_thư_mục_phân_loại
            destination_path = os.path.join("media_root", sub_folder)
            
            # Tiến hành gọi hàm tạo thư mục lưu trữ an toàn
            safe_create_dir(destination_path)
            
            # In kết quả xử lý thành công ra màn hình Console
            print(f"[TỆP TIN: {file_name}]")
            print(f" + Dung lượng thực tế: {actual_size:,} bytes")
            print(f" + Số khối phân vùng ({total_blocks} blocks) -> ĐẠT CHUẨN.")
            print(f" + Trạng thái phân loại:  Đã lưu vào thư mục '{destination_path}'")
            success_count += 1
            
        except ValueError:
            # Bắt gọn lỗi khi chuỗi ngày tháng không đúng thực tế (ví dụ: ngày 31 tháng 6)
            print(f"[TỆP TIN: {file_name}]")
            print(f" + Trạng thái phân loại: Thất bại (Lỗi định dạng ngày upload '{upload_date_str}' không tồn tại!)")
            
        print("-" * 64)
        
    # Báo cáo tổng kết tiến độ cuối cùng của ca làm việc
    print(f"TIẾN ĐỘ DUYỆT: Hoàn thành xử lý {success_count}/{total_count} tập tin thành công. Hệ thống ổn định.")


if __name__ == "__main__":
    main()