'''
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
'''
import math
def count_nums(summa, prod):
    disc = (summa ** 2) - (4 * prod)
    if disc > 0 and math.sqrt(disc)//int(math.sqrt(disc)) == 0:
        X = (summa + math.sqrt(disc))//2
        Y = (summa - math.sqrt(disc))//2
        print((X),(Y))
        return int(X),int(Y)
    else:
        print("Неправильные значения!")

summa = int(input("Сумма чисел: "))
prod = int(input("Произведение чисел: "))
count_nums(summa, prod)