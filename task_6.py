from itertools import count
from itertools import cycle

limit = 11
cnt = 0
for el in count(int(input("Введите число "))):
    cnt += 1
    print(el)
    if cnt >= limit:
        cnt = 0
        break

print("***************")

my_list = ("Hello", 15, 20, "Bye", True)
for el in cycle(my_list):
    cnt += 1
    print(el)
    if cnt >= limit:
        cnt = 0
        break
