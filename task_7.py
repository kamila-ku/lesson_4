from itertools import count
from math import factorial

h = int(input("Введите последнее число: "))
def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < h:
        print(i)
        x += 1
    else:
        break
