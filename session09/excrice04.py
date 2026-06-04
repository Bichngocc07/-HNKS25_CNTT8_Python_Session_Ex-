order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng (Menu con)")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")
    print("==================================================")
    
    main_choice = input("> Mời chọn chức năng (1-4): ").strip()
    print("-" * 50)
    
    if main_choice not in ["1", "2", "3", "4"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!\n")
        continue

    if main_choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.\n")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for i in range(len(order_list)):
                print(f"{i + 1}. {order_list[i]}")
            print("")

    
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
            
            if sub_choice not in ["1", "2", "3", "4"]:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!\n")
                continue
                
            if sub_choice == "1":
                new_id = input("Nhập mã đơn hàng mới (Ví dụ: ge004): ").strip().upper()
                new_status = input("Nhập trạng thái đơn hàng (PENDING/DELIVERING/COMPLETED/CANCELLED): ").strip().upper()
                
                new_order = f"{new_id} - {new_status}"
                order_list.append(new_order)
                print(f"=> Đã thêm đơn hàng mới thành công!\n")
                
            elif sub_choice == "2":
                if len(order_list) == 0:
                    print("Danh sách trống, không thể sửa!\n")
                    continue
                    
                pos_input = input(f"Nhập vị trí đơn hàng cần sửa (1 đến {len(order_list)}): ").strip()
                
                if not pos_input.isdigit():
                    print("Vị trí không hợp lệ!\n")
                    continue
                    
                index = int(pos_input) - 1
                
                if index < 0 or index >= len(order_list):
                    print(f"Không tìm thấy đơn hàng ở vị trí này!\n")
                    continue
                    
                new_id = input("Nhập mã đơn hàng mới: ").strip().upper()
                new_status = input("Nhập trạng thái mới: ").strip().upper()
                order_list[index] = f"{new_id} - {new_status}"
                print("=> Cập nhật thông tin đơn hàng thành công!\n")
                
            elif sub_choice == "3":
                if len(order_list) == 0:
                    print("Danh sách trống, không thể xóa!\n")
                    continue
                    
                pos_input = input(f"Nhập vị trí đơn hàng cần xóa (1 đến {len(order_list)}): ").strip()
                
                if not pos_input.isdigit():
                    print("Vị trí không hợp lệ!\n")
                    continue
                    
                index = int(pos_input) - 1
                
                if index < 0 or index >= len(order_list):
                    print(f"Không tìm thấy đơn hàng ở vị trí này!\n")
                    continue
                    
                removed_order = order_list.pop(index)
                print(f"=> Đã xóa thành công đơn hàng: {removed_order}\n")
                
            elif sub_choice == "4":
                print("Quay lại menu chính...\n")
                break

    elif main_choice == "3":
        pending_count = 0
        delivering_count = 0
        completed_count = 0
        cancelled_count = 0
        
        for order in order_list:
            parts = order.split("-")
            status = parts[1].strip()
            
            if status == "PENDING":
                pending_count += 1
            elif status == "DELIVERING":
                delivering_count += 1
            elif status == "COMPLETED":
                completed_count += 1
            elif status == "CANCELLED":
                cancelled_count += 1
                
        print("===== THỐNG KÊ ĐƠN HÀNG =====")
        print(f"PENDING: {pending_count}")
        print(f"DELIVERING: {delivering_count}")
        print(f"COMPLETED: {completed_count}")
        print(f"CANCELLED: {cancelled_count}")
        print(f"Tổng số đơn hàng: {len(order_list)}")
        print("=============================\n")

    
        print("Thoát chương trình.")
        print("Cảm ơn bạn đã sử dụng hệ thống điều phối Grab Express!")
        break # Thoát hẳn chương trình
