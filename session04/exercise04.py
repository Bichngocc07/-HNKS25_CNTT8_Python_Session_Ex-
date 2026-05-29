# Quy tắc 1 (Giới hạn lượt chơi): Mỗi khách hàng chỉ có tối đa 5 lần cơ hội để đưa ra dự đoán của mình.
# Quy tắc 2 (Gợi ý thông minh): Sau mỗi lần khách hàng nhập một số và đoán sai, máy tính phải thông báo cho khách hàng biết số họ vừa nhập đang lớn 
# hơn hay nhỏ hơn mã số may mắn của hệ thống để họ có cơ sở điều chỉnh ở lần đoán tiếp theo.
# Quy tắc 3 (Điểm dừng trò chơi): Trò chơi phải kết thúc lập tức ngay khi xảy ra một trong hai trường hợp: hoặc khách hàng
#  đã đoán chính xác mã số, hoặc khách hàng đã sử dụng hết cả 5 lượt đoán của mình.
# Quy tắc 4 (Thông báo kết quả): Khi trò chơi kết thúc, hệ thống dựa vào kết quả đoán của khách để đưa ra lời chào phù hợp: Hoặc chúc mừng 
# họ trúng thưởng quà đặc biệt, hoặc thông báo họ đã hết lượt và chúc may mắn lần sau.
number = 200
value = 0
while value < 5:
    value += 1
    is_number = int(input(f"Lượt đoán {value} - Nhập số của bạn: "))
    if is_number < number:
        print("=> Gợi ý: Số của bạn nhỏ hơn mã số may mắn!")
    elif is_number > number:
        print("=> Gợi ý: Số của bạn lớn hơn mã số may mắn!")
    else :
        print("=> Chúc mừng! Bạn đã đoán chính xác mã số may mắn!")
        break
print("--- TRÒ CHƠI KẾT THÚC ---")