input_month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
dict_month = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
list_month = ['winter', 'spring', 'summer', 'autumn']
if input_month == 1 or input_month == 2 or input_month == 12:

    print(dict_month.get(1))
    print(list_month[0])
elif input_month == 3 or input_month == 4 or input_month == 5:

    print(dict_month.get(2))
    print(list_month[1])
elif input_month == 6 or input_month == 7 or input_month == 8:

    print(dict_month.get(3))
    print(list_month[2])
elif input_month == 9 or input_month == 10 or input_month == 11:

    print(dict_month.get(4))
    print(list_month[3])
else:
    print('Такого месяца не существует в году!')
