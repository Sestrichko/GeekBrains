from itertools import cycle, count
# 1 скрипт

for i in count(2):
    if i == 10:
        break
    print(i)

# 2 скрипт
my_list = [1, 100, 9, 6, True, 'hello']
count = 0
for i in cycle([1, 2, 4, 100, 9, 6, True, 'hello']):
    if count == 10:
        break
    count += 1
    print(i)