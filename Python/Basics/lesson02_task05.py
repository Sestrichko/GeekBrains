my_list = [7, 5, 3, 3, 2, 1, 9]
num_input = int(input('Введите число: '))
my_list.append(num_input)
my_list.sort(reverse=True)
print(my_list)
print(type(my_list))