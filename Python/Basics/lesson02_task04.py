user_input = input('Введите несколько слов через пробел: ')
user_input = user_input.split(' ')
for ind, el in enumerate(user_input, 1):
    if len(el) > 10:
        print(ind, el[0:10])
    else:
        print(ind, el)