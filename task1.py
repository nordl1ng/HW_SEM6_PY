# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

a = int(input("Введите число: "))

import math
# list=[]
# for i in range(1,a+1):
#     list.append(math.factorial(i))
# print(list)

b=list(map(lambda x: math.factorial(x), range(1,a+1)))
print(b)
