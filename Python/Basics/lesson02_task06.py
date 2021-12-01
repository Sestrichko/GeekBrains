list_goods = []
dict_1 = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
dict_2 = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
i = 0

while True:
    if input('Для выхода из приложения нажмите Q, для продолжения Enter: '):
        break
    i += 1
    for num in dict_1.keys():
        prop = input(f'Введите значение свойства {num} ')
        dict_1[num] = int(prop) if num in ('цена', 'количество') else prop
        dict_2[num].append(dict_1[num])
    list_goods.append((i, dict_1.copy()))
    print(f"\nСтруктура товаров\n{list_goods}")
    print(f"\nТекущая аналитика по товарам:\n{'*'*30}")
    for key, value in dict_2.items():
        print(f"{key[:25]:>30}: {value}")
    print('*' * 30)

