proceeds = float(input('Введите сумму значения выручки: '))
costs = float(input('Введите сумму значения изжержек: '))

if proceeds > costs:
    profit_result = ((proceeds - costs) / proceeds)
    print(f'Фирма отработала с прибылью, рентабельность фирмы составляет: {profit_result * 100:.2f}%')
    number_workers = int(input('Введите количество сотрудников: '))
    profit_result_worker = profit_result / number_workers

    print(f'Рентабельность на одного сотрудника составляет: {profit_result_worker * 100:.2f}%')
else:
    print('Фирма отработала с убытками')
