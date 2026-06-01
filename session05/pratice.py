## cách dùng break
state = 1
cost = 0
while state > 0:
    state_name = f"State {state}"
    print({state_name})

    if state % 2!= 0:
        state += 1
        continue
    cost += 100_000
    if state == 5:
        break
#in bảng cửu chương từ 2 đén 9
for i in range(2, 10):
    print(f"Bảng cửu chương {i}:")
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print("-" * 30)

# Vẽ hình chữ nhật bằng dấu *
rows = 5   # số hàng (chiều cao)
cols = 10  # số cột (chiều rộng)

for i in range(rows):        # Outer loop: duyệt theo hàng
    for j in range(cols):    # Inner loop: duyệt theo cột
        print("*", end="")   # In dấu * trên cùng một dòng
    print()                  # Xuống dòng sau mỗi hàng

# Vẽ hình chữ nhật rỗng bằng dấu *
rows = 5   # số hàng (chiều cao)
cols = 10  # số cột (chiều rộng)
for i in range(rows):        # Outer loop: duyệt theo hàng
    for j in range(cols):    # Inner loop: duyệt theo cột
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")   # In dấu * nếu là hàng đầu, hàng cuối, cột đầu hoặc cột cuối
        else:
            if j == 0 or j == cols - 1:
                print("*", end="")   # In dấu * nếu là cột đầu hoặc cột cuối
            else:   
                print(" ", end="")   # In dấu cách nếu là phần bên trong
    print()                  # Xuống dòng sau mỗi hàng