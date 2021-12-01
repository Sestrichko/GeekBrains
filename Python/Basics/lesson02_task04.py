user_input = input('Введите несколько слов через пробел: ').split(' ')
for ind, el in enumerate(user_input, 1):
    print(ind, el[0:10])
