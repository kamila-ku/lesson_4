my_list = [10, 300, 2, 22, 44, 1, 1, 5, 10, 7, 1, 78, 123, 55]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num-1] < my_list[num] ]
print(my_list)
print(my_new_list)
