'''
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

Найдите количество и выведите его.

Пример:


list_1 = [1, 2, 3, 4, 5]
k = 3
# 1
'''


list_1 = [1, 2, 3, 4, 5]
k = int(input("Введите число, которое хотите найти: "))

def count_num(k, list_1):
    count = 0
    for i in range(len(list_1)):
        if k == list_1[i]:
            count+=1
    print(count)

count_num(k, list_1)