'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''

from random import randint

print(lst_1 := [randint(0, 10) for _ in range(int(input("Сколько элементов должно быть в первом множестве?\n")))])
print(lst_2 := [randint(0, 10) for _ in range(int(input("Сколько элементов должно быть во втором множестве?\n")))])
print(list(set(lst_1) & set(lst_2)))
