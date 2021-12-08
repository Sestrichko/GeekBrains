from itertools import count
from math import factorial


def func():
    for el in count(1):
        yield factorial(el)

val = func()
i = 1
for x in val:
    if i < 16:
        print(f'Факториал {i} равен: {x}')
        i += 1
    else:
        break



