my_list = [1, 4, 14, 14, 5, 1, 5, 7, 8, 5]
new_my_list = [el for el in my_list if my_list.count(el) < 2]

print(my_list)
print(new_my_list)
