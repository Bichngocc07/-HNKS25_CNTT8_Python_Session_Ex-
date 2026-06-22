# # Yêu cầu 1: Kỹ thuật Debugger & Viết Báo Cáo Phân Tích 
# # Không được sửa code trực tiếp ngay từ đầu và không dùng lệnh print(). Hãy chạy chương trình ở chế độ Debug mode trên IDE và hoàn thành các câu hỏi sau vào file báo cáo có dạng word:
# # Sử dụng Conditional Breakpoint: Mô tả cách thiết lập một Conditional Breakpoint tại hàm get_shipping_rate với điều kiện distance == 25. Khi chương trình dừng tại đây, hãy chụp ảnh màn hình hoặc ghi lại giá trị của biến base_rate trước
# # và sau khi chạy qua dòng điều kiện if distance >= 20:.
# # Debug luồng Logging: Giải thích tại sao dòng log logger.info(...) ở đầu hàm không hiển thị ra màn hình Console khi chạy thử? Cần sửa tham số gì ở hàm cấu hình logging.basicConfig() để nhìn thấy dòng log này?
# # Báo cáo lỗi: Chỉ rõ số dòng chứa lỗi logic tính sai phí phụ thu đường xa và giải thích tại sao lỗi đó lại xảy ra dựa trên kết quả quan sát từ Variables panel.
# # 1 
# 1. Sử dụng Conditional Breakpoint
# Cách thiết lập trên VS Code / Visual Studio:
# Mở file mã nguồn bằng IDE.
# Di chuột về phía bên trái của số dòng chứa lệnh if distance >= 20: (trong hàm get_shipping_rate), click chuột phải vào dấu chấm đỏ mờ và chọn Add Conditional Breakpoint... (hoặc chọn Expression).
# Nhập điều kiện: distance == 25 rồi nhấn Enter.
# Nhấn F5 để chạy chương trình ở chế độ Debug. IDE sẽ chỉ dừng lại ở dòng này khi distance có giá trị đúng bằng 25 (ở test case thứ nhất).
# Giá trị của biến base_rate trong vùng nhớ (Variables Panel):
# Trước khi chạy qua dòng base_rate = 10000: base_rate = 30000 (Giá gốc của phương thức express).
# Sau khi bước qua (Step Over - F10) dòng đó: base_rate = 10000.
# Hệ quả: Phí cơ sở bị giảm từ 30,000đ xuống còn 10,000đ thay vì được cộng thêm tiền.

# 2. Debug luồng Logging
# Nguyên nhân dòng log logger.info(...) không hiển thị: Do hệ thống hiện tại đang cấu hình mức log cơ sở là logging.WARNING (level=logging.WARNING). Theo cơ chế phân cấp của thư viện logging trong Python, hệ thống sẽ chỉ in ra các bản tin log có mức độ nghiêm trọng bằng hoặc cao hơn mức được cấu hình (tức là chỉ in WARNING, ERROR, CRITICAL). Bản tin INFO có cấp độ thấp hơn WARNING nên đã bị bộ lọc bỏ qua.
# Giải pháp sửa đổi: Cần thay đổi tham số cấu hình trong hàm logging.basicConfig() từ level=logging.WARNING thành level=logging.INFO.
# 3. Báo cáo lỗi logic
# Vị trí lỗi: Dòng code base_rate = 10000 bên trong khối điều kiện if distance >= 20:.
# Nguyên nhân: Lập trình viên thử việc đã sử dụng toán tử gán = thay vì toán tử cộng dồn +=. Lỗi này làm ghi đè hoàn toàn giá trị của base_rate đã tính toán được ở phía trên (ví dụ từ 30,000đ hoặc 50,000đ tụt xuống thẳng 10,000đ), dẫn đến việc khách hàng đi đường càng xa thì phí vận chuyển lại càng... rẻ bất thường.