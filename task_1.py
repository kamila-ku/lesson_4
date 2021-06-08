def salary():
    a = int(input("Выработка в часах: "))
    b = int(input("Ставка в час: "))
    c = int(input("Премия: "))
    return a * b + c

print(f'Заработная плата составила: {salary() }')
