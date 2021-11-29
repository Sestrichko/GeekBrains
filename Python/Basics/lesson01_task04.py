user_number = abs(int(input('Введите целое положительное число: ')))
max_num = user_number % 10

while user_number > 0:
    user_number = user_number // 10
    if user_number % 10 > max_num:
        max_num = user_number % 10
    user_number = user_number // 10

print('Максимальная цифра в числе: ', max_num)



