'''
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

Пример:
'''

list_1 = [1, 12, 6, 7, 8, 15]
k = 11
# 5

lst_dif = []
for i in range(len(list_1)):
    if k > list_1[i]:
        lst_dif.append(k - list_1[i])
    else:
        lst_dif.append(list_1[i] - k)
print(list_1[lst_dif.index(min(lst_dif))])





