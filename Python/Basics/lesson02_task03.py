month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
dict_month = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
list_month = ['winter', 'spring', 'summer', 'autumn']
if month == 1 or month == 2 or month == 12:

    print(dict_month.get(1))
    print(list_month[0])
elif month == 3 or month == 4 or month == 5:

    print(dict_month.get(2))
    print(list_month[1])
elif month == 6 or month == 7 or month == 8:

    print(dict_month.get(3))
    print(list_month[2])
elif month == 9 or month == 10 or month == 11:

    print(dict_month.get(4))
    print(list_month[3])
else:
    print('Такого месяца не существует в году!')
