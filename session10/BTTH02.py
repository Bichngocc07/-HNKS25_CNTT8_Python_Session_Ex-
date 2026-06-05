playlist = []

while True:
    print("\n========== MENU QUẢN LÝ DANH SÁCH PHÁT ==========")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và trích xuất danh sách")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ")

    # Chức năng 1
    if choice == "1":
        print("\n--- THÊM BÀI HÁT ---")
        print("1. Thêm vào cuối danh sách")
        print("2. Thêm vào vị trí cụ thể")

        sub_choice = input("Nhập lựa chọn: ")
        song = input("Nhập tên bài hát: ")

        if sub_choice == "1":
            playlist.append(song)
            print("Thêm bài hát thành công!")
            print("Tổng số bài hát:", len(playlist))

        elif sub_choice == "2":
            try:
                index = int(input("Nhập vị trí muốn chèn: "))

                if 0 <= index <= len(playlist):
                    playlist.insert(index, song)
                    print("Thêm bài hát thành công!")
                    print("Tổng số bài hát:", len(playlist))
                else:
                    print("Vị trí không hợp lệ!")

            except ValueError:
                print("Vui lòng nhập số nguyên!")

        else:
            print("Lựa chọn không hợp lệ!")

    # Chức năng 2
    elif choice == "2":
        print("\n===== DANH SÁCH PHÁT =====")

        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
        else:
            for i, song in enumerate(playlist, start=1):
                print(f"{i}. {song}")

            print("\nTổng số bài hát:", len(playlist))

    # Chức năng 3
    elif choice == "3":
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("\n--- XÓA BÀI HÁT ---")
        print("1. Xóa theo tên bài hát")
        print("2. Xóa theo chỉ số")

        sub_choice = input("Nhập lựa chọn: ")

        if sub_choice == "1":
            song_name = input("Nhập tên bài hát cần xóa: ")

            if song_name in playlist:
                playlist.remove(song_name)
                print(f"Đã xóa bài hát [{song_name}] khỏi danh sách!")
            else:
                print("Không tìm thấy bài hát trong danh sách phát!")

        elif sub_choice == "2":
            try:
                index = int(input("Nhập vị trí cần xóa: "))

                if 0 <= index < len(playlist):
                    removed_song = playlist.pop(index)
                    print(f"Đã xóa bài hát [{removed_song}] khỏi danh sách!")
                else:
                    print("Vị trí không hợp lệ!")

            except ValueError:
                print("Vui lòng nhập số nguyên!")

        else:
            print("Lựa chọn không hợp lệ!")

    # Chức năng 4
    elif choice == "4":
        if len(playlist) == 0:
            print("Danh sách phát hiện đang trống!")
            continue

        print("\n--- SẮP XẾP VÀ TRÍCH XUẤT DANH SÁCH ---")
        print("1. Sắp xếp danh sách phát theo bảng chữ cái A-Z")
        print("2. Hiển thị 3 bài hát đầu tiên")

        sub_choice = input("Nhập lựa chọn: ")

        if sub_choice == "1":
            playlist.sort()

            print("\nDanh sách sau khi sắp xếp:")
            for i, song in enumerate(playlist, start=1):
                print(f"{i}. {song}")

        elif sub_choice == "2":
            print("\n3 bài hát đầu tiên:")

            for i, song in enumerate(playlist[:3], start=1):
                print(f"{i}. {song}")

        else:
            print("Lựa chọn không hợp lệ!")

    # Chức năng 5
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên từ 1 đến 5!")
        