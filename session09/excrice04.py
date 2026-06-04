# Khởi tạo danh sách đơn hàng ban đầu theo cấu trúc "MÃĐƠNHÀNG - TRẠNGTHÁI"
order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

# Vòng lặp chính điều hướng Menu chính
while True:
    print("===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng (Menu con)")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")
    print("==================================================")
    
    main_choice = input("> Mời chọn chức năng (1-4): ").strip()
    print("-" * 50)
    
    # --- BẪY 4: Kiểm tra lựa chọn menu chính không hợp lệ ---
    if main_choice not in ["1", "2", "3", "4"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!\n")
        continue

    # =========================================================================
    # CHỨC NĂNG 1: HIỂN THỊ DANH SÁCH ĐƠN HÀNG
    # =========================================================================
    if main_choice == "1":
        # Kiểm tra danh sách rỗng
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.\n")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for i in range(len(order_list)):
                # Hiển thị số thứ tự thân thiện với người dùng (bắt đầu từ 1)
                print(f"{i + 1}. {order_list[i]}")
            print("") # Xuống dòng cho thoáng

    # =========================================================================
    # CHỨC NĂNG 2: CẬP NHẬT DANH SÁCH ĐƠN HÀNG (SUB-MENU)
    # =========================================================================
    elif main_choice == "2":
        while True:
            print("----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
            print("1. Thêm đơn hàng mới")
            print("2. Sửa đơn hàng theo vị trí")
            print("3. Xóa đơn hàng theo vị trí")
            print("4. Quay lại menu chính")
            print("---------------------------------------")
            
            sub_choice = input("> Mời chọn chức năng cập nhật (1-4): ").strip()
            print("-" * 40)
            
            # Kiểm tra lựa chọn menu con không hợp lệ
            if sub_choice not in ["1", "2", "3", "4"]:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!\n")
                continue
                
            # --- 2.1. Thêm đơn hàng mới ---
            if sub_choice == "1":
                new_id = input("Nhập mã đơn hàng mới (Ví dụ: ge004): ").strip().upper()
                new_status = input("Nhập trạng thái đơn hàng (PENDING/DELIVERING/COMPLETED/CANCELLED): ").strip().upper()
                
                # Định dạng chuẩn: "MÃĐƠNHÀNG - TRẠNGTHÁI"
                new_order = f"{new_id} - {new_status}"
                order_list.append(new_order)
                print(f"=> Đã thêm đơn hàng mới thành công!\n")
                
            # --- 2.2. Sửa đơn hàng theo vị trí ---
            elif sub_choice == "2":
                if len(order_list) == 0:
                    print("Danh sách trống, không thể sửa!\n")
                    continue
                    
                pos_input = input(f"Nhập vị trí đơn hàng cần sửa (1 đến {len(order_list)}): ").strip()
                
                # --- BẪY 3: Kiểm tra người dùng nhập chữ thay vì số vị trí ---
                if not pos_input.isdigit():
                    print("Vị trí không hợp lệ!\n")
                    continue
                    
                # Chuyển sang số nguyên và trừ đi 1 để ra chỉ số Index của Python
                index = int(pos_input) - 1
                
                # --- BẪY 2: Kiểm tra vị trí vượt quá phạm vi của mảng ---
                if index < 0 or index >= len(order_list):
                    print(f"Không tìm thấy đơn hàng ở vị trí này!\n")
                    continue
                    
                # Tiến hành sửa nếu vị trí hợp lệ
                new_id = input("Nhập mã đơn hàng mới: ").strip().upper()
                new_status = input("Nhập trạng thái mới: ").strip().upper()
                order_list[index] = f"{new_id} - {new_status}"
                print("=> Cập nhật thông tin đơn hàng thành công!\n")
                
            # --- 2.3. Xóa đơn hàng theo vị trí ---
            elif sub_choice == "3":
                if len(order_list) == 0:
                    print("Danh sách trống, không thể xóa!\n")
                    continue
                    
                pos_input = input(f"Nhập vị trí đơn hàng cần xóa (1 đến {len(order_list)}): ").strip()
                
                # Kiểm tra bẫy nhập chữ
                if not pos_input.isdigit():
                    print("Vị trí không hợp lệ!\n")
                    continue
                    
                index = int(pos_input) - 1
                
                # Kiểm tra bẫy vị trí ngoài phạm vi mảng
                if index < 0 or index >= len(order_list):
                    print(f"Không tìm thấy đơn hàng ở vị trí này!\n")
                    continue
                    
                # Thực hiện xóa đơn hàng bằng phương thức pop
                removed_order = order_list.pop(index)
                print(f"=> Đã xóa thành công đơn hàng: {removed_order}\n")
                
            # --- 2.4. Quay lại menu chính ---
            elif sub_choice == "4":
                print("Quay lại menu chính...\n")
                break # Bẻ gãy vòng lặp menu con để quay về menu ngoài

    # =========================================================================
    # CHỨC NĂNG 3: THỐNG KÊ ĐƠN HÀNG THEO TRẠNG THÁI
    # =========================================================================
    elif main_choice == "3":
        # Khởi tạo các biến đếm trạng thái ban đầu bằng 0
        pending_count = 0
        delivering_count = 0
        completed_count = 0
        cancelled_count = 0
        
        # Duyệt qua từng đơn hàng để bóc tách chuỗi bằng dấu gạch ngang "-"
        for order in order_list:
            # Tách chuỗi làm 2 phần: [Mã đơn, Trạng thái]
            parts = order.split("-")
            # Lấy phần tử thứ 2 (index 1) và làm sạch khoảng trắng
            status = parts[1].strip()
            
            # Cộng dồn vào biến đếm tương ứng
            if status == "PENDING":
                pending_count += 1
            elif status == "DELIVERING":
                delivering_count += 1
            elif status == "COMPLETED":
                completed_count += 1
            elif status == "CANCELLED":
                cancelled_count += 1
                
        # Hiển thị bảng báo cáo thống kê cuốn chiếu
        print("===== THỐNG KÊ ĐƠN HÀNG =====")
        print(f"PENDING: {pending_count}")
        print(f"DELIVERING: {delivering_count}")
        print(f"COMPLETED: {completed_count}")
        print(f"CANCELLED: {cancelled_count}")
        print(f"Tổng số đơn hàng: {len(order_list)}")
        print("=============================\n")

    # =========================================================================
    # CHỨC NĂNG 4: THOÁT CHƯƠNG TRÌNH
    # =========================================================================
    elif main_choice == "4":
        print("Thoát chương trình.")
        print("Cảm ơn bạn đã sử dụng hệ thống điều phối Grab Express!")
        break # Thoát hẳn chương trình