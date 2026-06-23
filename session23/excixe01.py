import os
import math
from datetime import datetime, timedelta


shipments = [
    {
        "id": "TRK-001", 
        "from_lat": "21.0285", "from_lon": "105.8542", 
        "to_lat": "10.8231", "to_lon": "106.6297", 
        "depart": "2026-06-23 08:00:00", "deadline": "2026-06-24 12:00:00"
    },
    {
        "id": "TRK-002", 
        "from_lat": "21.0285", "from_lon": "105.8542", 
        "to_lat": "16.0544", "to_lon": "108.2022", 
        "depart": "2026-06-23 08:00:00", "deadline": "2026-06-23 18:00:00"
    }
]



def create_log_dir(dir_name="logs"):
    """Kiểm tra và tạo thư mục một cách an toàn để tránh lỗi trùng lặp."""
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def calculate_distance(lat1, lon1, lat2, lon2):
    """Tính khoảng cách giữa 2 tọa độ trên mặt cầu theo công thức Haversine."""
    flat_lat1 = math.radians(float(lat1))
    flat_lon1 = math.radians(float(lon1))
    flat_lat2 = math.radians(float(lat2))
    flat_lon2 = math.radians(float(lon2))
    
    R = 6371.0
    
    dlat = flat_lat2 - flat_lat1
    dlon = flat_lon2 - flat_lon1
    
    a = (math.sin(dlat / 2) ** 2 + 
         math.cos(flat_lat1) * math.cos(flat_lat2) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    return round(distance, 2)


def predict_eta(departure_str, distance_km, speed_kph=60):
    """Tính thời gian dự kiến đến nơi (ETA) dựa vào khoảng cách và vận tốc."""
    dep_time = datetime.strptime(departure_str, "%Y-%m-%d %H:%M:%S")
    
    hours_needed = distance_km / speed_kph
    
    eta_time = dep_time + timedelta(hours=hours_needed)
    return eta_time



def main():
    create_log_dir("logs")
    
    print("======== HỆ THỐNG ĐIỀU PHỐI VẬN TẢI RIKKEI LOGISTICS ========")
    print("[INFO] Khởi tạo hệ thống lịch trình vận tải hành trình... THÀNH CÔNG.")
    print("----------------------------------------------------------------")
    
    for shipment in shipments:
        s_id = shipment["id"]
        
        distance = calculate_distance(
            shipment["from_lat"], shipment["from_lon"],
            shipment["to_lat"], shipment["to_lon"]
        )
        
        eta = predict_eta(shipment["depart"], distance)
        
        deadline_time = datetime.strptime(shipment["deadline"], "%Y-%m-%d %H:%M:%S")
        
        if eta <= deadline_time:
            status = "AN TOÀN (Kịp tiến độ trước deadline)"
        else:
            status = "CẢNH BÁO (Trễ hạn deadline yêu cầu của khách hàng)"
            
        print(f"[{s_id}]")
        print(f" + Khoảng cách vận chuyển: {distance:,} km")
        print(f" + Thời gian khởi hành: {shipment['depart']}")
        print(f" + Dự kiến cập bến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f" + Trạng thái: {status}")
        print("-" * 64)


if __name__ == "__main__":
    main()
