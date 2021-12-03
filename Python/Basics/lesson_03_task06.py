def int_func(arg_1, arg_2, arg_3):
    """ Функция принимает строку из слов, разделенных пробелом, в нижнем регистре
    Функция возвращает слова с заглавной буквы
    """

    word = ' '.join([arg_1, arg_2, arg_3])
    return word.title()
word_1 = input('Введите первое слово: ')
word_2 = input('Введите второе слово: ')
word_3 = input('Введите третье слово: ')


print(int_func(arg_1=word_1, arg_2=word_2, arg_3=word_3))