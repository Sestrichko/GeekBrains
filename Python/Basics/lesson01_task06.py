a = float(input('Введите количество километров за первый день пробежки: '))
b = float(input('Введите желаемый результат километров к преодолению: '))
result_km = a
result_day = 1
while result_km < b:
    result_km = result_km + result_km * 0.1
    result_day = result_day + 1
    if result_km > b:
        break
print('На', result_day, 'день спортсмен пробежит не менее ', b, ' км')

