# + remove(value) => Xóa phần tử có giá trị value đầu tiên trong list
# + pop(index) => Xóa phần tử ở vị trí index và trả về giá trị của phần tử đó
# + clear() => Xóa tất cả phần tử trong list
# + del list[index] => Xóa phần tử ở vị trí index
# + del list[:] => Xóa toàn bộ list khỏi bộ nhớ

# +pop(index)
# Xóa phần tử ở vị trí index


name_array = ["Bít Ngọt", "Huy", "Hùng"]
name_array.remove("Bít Ngọt")
print(name_array)


#Pop()method
name_array.pop(1)
print(name_array)

#del method[i]
del name_array[1]
print(name_array)