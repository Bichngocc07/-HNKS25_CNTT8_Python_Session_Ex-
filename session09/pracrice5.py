#Lấy theo index-value
for i in range(len(name_array)):
    print(f"Index: {i}, Value: {name_array[i]}")
print()

# #Sử dụng enumerate()
for i, value in enumerate(name_array):
    print(f"{i} - {value}")
print()

for value in enumerate(name_array):
    print(f"{value}")