'''
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

Пример:
'''


from random import randint

print(list_1 := [randint(0, 10) for _ in range(int(input("Сколько элементов должно быть в первом множестве?\n")))])
k = int(input("К  какому числу нужно найти ближайший элемент?\n"))
# 5

lst_dif = []
for i in range(len(list_1)):
    if k > list_1[i]:
        lst_dif.append(k - list_1[i])
    else:
        lst_dif.append(list_1[i] - k)
print(list_1[lst_dif.index(min(lst_dif))])





