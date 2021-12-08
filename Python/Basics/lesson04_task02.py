my_list = [2, 6, 3, 90, 1, 77, 5, 3, 100]
my_list_new = [el for i, el in enumerate(my_list) if my_list[i - 1] < my_list[i]]

print(my_list_new)