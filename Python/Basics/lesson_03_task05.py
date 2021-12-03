def input_sum():
    sum_res = 0
    while True:
        number_list = input('Введите числа или Q для выхода из программы: ').split()
        for el in number_list:
            if el == 'Q':
                return sum_res
            else:
                sum_res += int(el)

        print(f'Текущая сумма чисел равна: {sum_res}')

print(f'Окончательная сумма равна {input_sum()}')
