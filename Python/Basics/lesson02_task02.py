user_count = int(input('Введите количество значений списка: '))
my_List = []
i = 0
el = 0
while i < user_count:
    num = input(f'Введите значение {i} элемента: ')
    my_List.append(num)
    i += 1
print('Оригинальный список: ', my_List)

for i in range(0, len(my_List)-1, 2):
    my_List[i], my_List[i+1] = my_List[i+1], my_List[i]

print('Новый список: ', my_List)
