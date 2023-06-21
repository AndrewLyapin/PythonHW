'''
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
'''

def broke(rows, col):
    slice = int(input("Сколько долек нужно?\n"))
    if slice > 0:
        if rows*col <= 0:
            print("Такой шоколадки быть не может")
        elif slice <= rows * col:
            if slice % col == 0 or slice % rows == 0:
                print(f'{rows} {col} {slice} -> yes')
            else:
                print(f'{rows} {col} {slice} -> no')
        else:
            print("Столько долек там нет")
    else:
        print("Вы хотите приклеить дольки к шоколаду?)")

rows = int(input("Сколько долек по ширине?\n"))

if rows > 0:
    col = int(input("Сколько долек по длине?\n"))
    if col > 0:
        broke(rows, col)
    else:
        print("Такой шоколадки быть не может")
else:
    print("Такой шоколадки быть не может")