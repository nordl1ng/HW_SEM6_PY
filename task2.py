# 1 . Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input("Введите число, обозначающее день недели: "))
# if day == 6 or day == 7:
#     print("Да, выходной")
# else:
#     print("Нет, будний день")
    
week = (lambda day: "Да, выходной" if (day == (6 or 7)) else "Нет, будний день")
print(week (day))