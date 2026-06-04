# #Thêm append,insert, remove, pop, clear, count, index, sort, reverse
# +list.append(value) => Thêm 1 phần tử vào cuối list
# +list.insert(index, value) => Thêm value vào vị trí index 
# +list.remove(listB) 
# +listA.extend(listB) => Thêm tất cả phần tử của listB vào cuối listA


score_list = [9, 8, 7]
print(f"score_list = {score_list}")

#Thêm 1 phần tử vào list
score_list_append = (0)
print(score_list)

#Thêm 1 phần tử vào list ở vị trí index và list
score_list_insert = ("Bít Ngọt")
print(score_list)

#List thêm vào list
listA = [1, 2, 3]
listB = ["Tung", "Hùng", "Hải"]
listA.append(listB)
print(listA)

#Sửa
name_list = ["Tung", "Hùng", "Hải"]
name_list[0] = "Bít Ngọt"
print(name_list)

#Xóa
name_list = ["Tung", "Hùng", "Hải"]
name_list.remove("Hùng")
print(name_list)

