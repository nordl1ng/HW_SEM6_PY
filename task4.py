# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример
# - [2, 3, 5, 9, 3] - на нечётных позициях элементы 3 и 9, ответ 12

listt=[2, 7, 5, 9, 3]

# def summ_not_ev(list):
#     summ = int (0)
#     for i in range(1,len(list),2):
#             summ += list[i]
#     print(f'Сумма элементов на нечетных позициях равна {summ}')

# summ_not_ev(listt)

new_list = sum(filter(lambda val: listt.index(val) % 2 != 0, listt))

print(new_list)
