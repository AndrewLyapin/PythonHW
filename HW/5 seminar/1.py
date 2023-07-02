'''
Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
'''

def pow_nums(num, pow_num, num_):
    if pow_num == 1:
        return num
    else:
        num = num * num_
        return pow_nums(num, pow_num - 1, num_)

num = int(input("Какое число возвести?\n"))
num_ = num
pow_num = int(input("В какую степень?\n"))
print(pow_nums(num, pow_num, num_))