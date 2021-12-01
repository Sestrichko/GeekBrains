my_list = [7, 5, 3, 3, 2, 1]
num_input = int(input('Введите число: '))
i = 0

for num in my_list:
    if num_input <= num:
        i += 1
    elif num_input > num:
        break

my_list.insert(i, num_input)
print(my_list)
