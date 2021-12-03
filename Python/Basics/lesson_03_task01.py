def func_div(*args):
    """Возвращает частное от деления

    Позиционнные параметры:
    var_1 -- делимое (int)
    var_2 -- делитель (int)
    if var_2 != 0
        return var_1/var_2
    elif var_1 or var_2 != int
        print("Неверный ввод значения числа!")
    else:
        print("Делитель не может быть ноль")

    """
    try:
        var_1 = int(input('Введите первое число: '))
        var_2 = int(input('Введите второе число: '))
        div_var = var_1 / var_2
    except ZeroDivisionError:
        print("Делитель не может быть ноль")
    except ValueError:
        print("Неверный ввод значения числа!")

    return div_var


print(f'Результат деления равен: {func_div():.2f}')

