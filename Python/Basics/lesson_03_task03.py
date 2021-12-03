def my_func(var_1, var_2, var_3):
    """Возвращает сумму наибольших двух аргументов

    Позиционнные параметры

    """
    list_var = [var_1, var_2, var_3]
    min_var = min(list_var)
    new_my_list = []
    for item in list_var:
        if item != min_var:
            new_my_list.append(item)
    arg_1 = new_my_list[0]
    arg_2 = new_my_list[1]
    result = arg_1 + arg_2
    return result


print(my_func(3, 5, 8))