name_array = ["Bít Ngọt", "Huy", "Hùng"]

#Duyệt phần tử trong list
length_nme_array = len(name_array)
print(name_array[0]) #Bít Ngọt
print(name_array[1]) #Huy
print(name_array[2]) #Hùng


# for i in range( start , stop , step ):
#     #Thực hiện câu lệnh

#Cách 1: Duyệt theo index
for idx in range(len(name_array)):
    print(name_array[idx])
print()
#Cách 2: Duyệt theo value
for name in name_array:
    print(name)
print()
#Duyệt danh sách những sinh viên bằng chữ "T"
for value in name_array:
    # if"T" in value:
    #     print(value)
    if value.startswith("T"):
        print(value)
##Duyệt phần tử trong mảng bằng while
print("Duyệt phần tử trong mảng bằng while")
I = 0
