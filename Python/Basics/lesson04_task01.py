from sys import argv

my_product, my_rate, my_prize = map(int, argv[1:4])

def my_wage():
    print(f'Заработная плата составляет:  {my_product * my_rate + my_prize}')

my_wage()