my_list = ['hello', 123, True, 34.5, complex(10, 5), None, (), {}, [], range(7), bytearray(b'text'), frozenset(),
           b'text']
for el in my_list:
    print(f'{el} - {type(el)}')
    