from functools import reduce
my_list = range(99,1001)
new_list = [el for el in my_list if el % 2 == 0]
multi = reduce(lambda x,y: x * y, new_list)
print(new_list)
print(multi)
