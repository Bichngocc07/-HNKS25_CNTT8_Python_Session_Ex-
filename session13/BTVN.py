# Khởi tạo cấu trúc dữ liệu: List chứa các Dictionary (Dữ liệu dùng Tiếng Anh)
parking_lot = []
id_counter = 1

# Định nghĩa giá vé gửi xe
BIKE_FARE = 5000
CAR_FARE = 20000

while True:
    print("\n" + "="*45)
    print("      HỆ THỐNG QUẢN LÝ BÃI ĐỖ XE THÔNG MINH      ")
    print("="*45)
    print("1. Check-in (Đón xe vào)")
    print("2. Báo cáo tồn kho (Danh sách xe)")
    print("3. Tìm kiếm xe theo biển số")
    print("4. Check-out (Trả xe & Tính phí)")
    print("5. Thoát chương trình")
    print("="*45)
    
    # Bắt lỗi nhập Menu trống 
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    if not choice:
        print("Dữ liệu không được để trống. Vui lòng nhập lại!")
        continue
    # 1. CHECK-IN (ĐÓN XE VÀO)
    if choice == '1':
        print("\n--- CHỨC NĂNG CHECK-IN ---")
        
        # Nhập biển số xe (Không để trống)
        while True:
            plate = input("Nhập biển số xe: ").strip().upper()
            if plate:
                break
            print("Dữ liệu không được để trống. Vui lòng nhập lại!")
            
        # Kiểm tra xem biển số đã có trong bãi chưa
        is_duplicate = False
        for vehicle in parking_lot:
            if vehicle['plate'] == plate:
                is_duplicate = True
                break
        if is_duplicate:
            print(f"Biển số {plate} đã tồn tại trong bãi xe!")
            continue

        # Nhập loại xe (Chỉ nhận 1 hoặc 2)
        while True:
            type_input = input("Chọn loại xe (1: Xe máy, 2: Ô tô): ").strip()
            if not type_input:
                print("Dữ liệu không được để trống!")
                continue
            if type_input in ['1', '2']:
                vehicle_type = "Motorbike" if type_input == '1' else "Car"
                break
            print("Loại xe không hợp lệ! Chỉ chọn 1 (Xe máy) hoặc 2 (Ô tô).")

        # Nhập giờ vào bãi bằng .isdigit() 
        while True:
            entry_input = input("Nhập giờ vào bãi (0-23): ").strip()
            if not entry_input:
                print("Dữ liệu không được để trống!")
                continue
            
            if entry_input.isdigit():
                entry_time = int(entry_input)
                if 0 <= entry_time <= 23:
                    break
                else:
                    print("Giờ vào phải nằm trong khoảng từ 0 đến 23.")
            else:
                print("Sai kiểu dữ liệu! Vui lòng nhập một số nguyên.")

        # Thêm xe mới vào List 
        new_vehicle = {
            "id": id_counter,
            "plate": plate,
            "type": vehicle_type,
            "entry_time": entry_time
        }
        parking_lot.append(new_vehicle)
        print(f"Check-in thành công! Xe đã được cấp ID: {id_counter}")
        id_counter += 1 

    # 2. BÁO CÁO TỒN KHO
    elif choice == '2':
        print("\n--- BÁO CÁO TỒN KHO ---")
        if len(parking_lot) == 0:
            print("Hiện tại bãi xe trống (Không có dữ liệu tồn kho).")
        else:
            print("-" * 55)
            print(f"{'ID':<6} | {'Biển số xe':<15} | {'Loại xe':<12} | {'Giờ vào':<8}")
            print("-" * 55)
            for vehicle in parking_lot:
                type = "Xe máy" if vehicle['type'] == "Motorbike" else "Ô tô"
                print(f"{vehicle['id']:<6} | {vehicle['plate']:<15} | {type:<12} | {vehicle['entry_time']:<8}h")
            print("-" * 55)
            print(f"Tổng số xe hiện tại trong bãi: {len(parking_lot)}")

    # 3. TÌM KIẾM XE
    elif choice == '3':
        print("\n--- TÌM KIẾM XE ---")
        while True:
            search_plate = input("Nhập biển số xe cần tìm: ").strip().upper()
            if search_plate:
                break
            print("Dữ liệu không được để trống!")
            
        found_vehicle = None
        for vehicle in parking_lot:
            if vehicle['plate'] == search_plate:
                found_vehicle = vehicle
                break
                
        if found_vehicle:
            print("\n[ĐÃ TÌM THẤY THÔNG TIN XE]")
            print(found_vehicle) 
        else:
            print(f"Không tìm thấy xe có biển số {search_plate} trong bãi!")

    # 4. CHECK-OUT & TÍNH TIỀN
    elif choice == '4':
        print("\n--- CHỨC NĂNG CHECK-OUT ---")
        while True:
            checkout_plate = input("Nhập biển số xe muốn check-out: ").strip().upper()
            if checkout_plate:
                break
            print("Dữ liệu không được để trống!")
            
        # Tìm xe trong bãi
        target_vehicle = None
        for vehicle in parking_lot:
            if vehicle['plate'] == checkout_plate:
                target_vehicle = vehicle
                break
                
        if target_vehicle is None:
            print(f"Không tìm thấy xe có biển số {checkout_plate} để thanh toán!")
            continue

        # Nhập và kiểm tra giờ ra
        while True:
            exit_input = input("Nhập giờ ra khỏi bãi (0-23): ").strip()
            if not exit_input:
                print("Dữ liệu không được để trống!")
                continue
                
            if exit_input.isdigit():
                exit_time = int(exit_input)
                if 0 <= exit_time <= 23:
                    # Bẫy lỗi logic giờ ra nhỏ hơn giờ vào
                    if exit_time >= target_vehicle['entry_time']:
                        break
                    else:
                        print(f"Giờ ra ({exit_time}h) không được nhỏ hơn Giờ vào ({target_vehicle['entry_time']}h)!")
                else:
                    print("Giờ ra phải nằm trong khoảng từ 0 đến 23.")
            else:
                print("Sai kiểu dữ liệu! Vui lòng nhập một số nguyên.")

        # Tính toán thời gian gửi xe
        duration = exit_time - target_vehicle['entry_time']
        if duration == 0:
            duration = 1 
            
        fare_rate = BIKE_FARE if target_vehicle['type'] == "Motorbike" else CAR_FARE
        total_fee = duration * fare_rate
        
        # In hóa đơn
        print("\n" + "-"*40)
        print(" ----- HÓA ĐƠN THANH TOÁN GỬI XE -----")
        print("-"*40)
        print(f"Biển số xe: {target_vehicle['plate']}")
        type = "Xe máy" if target_vehicle['type'] == "Motorbike" else "Ô tô"
        print(f"Loại xe:    {type}")
        print(f"Thời gian:  {target_vehicle['entry_time']}h -> {exit_time}h ({duration} giờ)")
        print(f"Thành tiền: {total_fee:,} VND")
        print("-"*40)
    
        # Xóa xe khỏi List bãi đỗ
        parking_lot.remove(target_vehicle)
        print("Xe đã thanh toán thành công và rời khỏi bãi!")
    # 5. THOÁT
    elif choice == '5':
        print("Đã thoát hệ thống. Cảm ơn bạn đã sử dụng chương trình!")
        break
    else :
        print("Lựa chọn không hợp lệ")
