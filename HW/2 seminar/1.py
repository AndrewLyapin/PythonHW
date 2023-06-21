'''
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
'''


from random import randint
def count_side(coin):
    count_eagle = 0
    count_tails = 0

    for side in range(coin):
        side = randint(0, 1)
        if side == 0:
            print('Орел', end=' ')
            count_eagle += 1
        else:
            print('Решка', end=' ')
            count_tails += 1

    if count_eagle >= count_tails:
        print(f'\nНужно перевернуть Решку {count_tails} раз')
    else:
        print(f'\nНужно перевернуть Орла {count_eagle} раз')

coin = int(input("Сколько раз бросали монетку? \n"))
count_side(coin)