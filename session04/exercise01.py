# Chức năng 1: Cho phép thu ngân nhập vào tổng số tiền ban đầu của hóa đơn (số nguyên).
# Chức năng 2: Áp dụng các kiến thức đã học để tính số tiền giảm giá:
# Nếu hóa đơn từ 500,000 VND trở lên: Giảm 10% trên tổng số tiền.
# Nếu hóa đơn dưới 500,000 VND: Không được giảm giá (Giảm 0%).
# Chức năng 3: Tính toán số tiền thực tế khách phải trả (Tổng tiền 
# ban đầu trừ đi số tiền giảm giá) và in kết quả ra màn hình.

#Input số tiền ban đầu 
#Ouput số tiền thực khách phải trả
#Process 
#Tính số tiền giảm giá dựa trên điều kiện (if-else).Công thức: Tổng tiền bann đầu * 0.1
#Tính số tiền thực khách phải trả: Tổng tiền ban đầu - Số tiền giảm giá
print("----- Nhập số tiền hóa đơn ban đầu -----")
total_amount = int(input("Nhập tổng số tiền hóa đơn: "))
if total_amount >= 500000: # nếu mà tổng chi tiêu lớn hơn bằng 500
    discount = total_amount * 0.1
    #discount là số tiền giảm giá
else:
    discount = 0
total_amount = total_amount - discount
#total_amount là tính giá tiền sau khi giảm giá
print("Tổng tiền khách phải trả :", total_amount)