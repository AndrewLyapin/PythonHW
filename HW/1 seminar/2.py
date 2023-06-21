'''
Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
'''



def count_birds(birds):
    Kate = int(birds * 0.67)
    PetrAndSerj = (int(birds * 0.335))//2
    dif = Kate - ((PetrAndSerj*2) * 2)
    if dif == 0:
        print(f'{birds} -> {PetrAndSerj} {Kate} {PetrAndSerj}')
    else:
        print(f'{birds} -> {PetrAndSerj} {Kate} {PetrAndSerj} \nКатя сделала за лентяев еще {dif} Журавликов')

birds = int(input("Сколько Журавликов сделано?\n"))
count_birds(birds)


