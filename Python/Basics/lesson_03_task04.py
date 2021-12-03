def my_func(x, y):
    """ Программа возвращает число x в степени y
    Решить двумя способами

    Позиционные параметры
    :param x: действительное положительное число
    :param y: целое отрицательное число
    """
# 1-й способ:
    my_pow = x ** y
    if x <= 0 or y >= 0:
        print('Ошибка, некорректный ввод х и/или y')
    else:
        return my_pow


result = my_func(2, -1)
print(result)
# 2-й способ:
def my_func(x, y):
    if x <= 0 or y >= 0:
        print('Ошибка, некорректный ввод х и/или y')
    else:
        result = 1
        for num in range(abs(y)):
            result *= x
            return 1 / result


result = my_func(2, -1)
print(f'Возведение в степень циклом {result}')


