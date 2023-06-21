'''
Вы пользуетесь общественным транспортом? Вероятно,
вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''


def check_luck(ticket):
    dig_lst1_part = []
    dig_lst2_part = []
    for digit in range(3):
        dig_lst1_part.append(int(ticket[digit]))

    for digit in range(3, len(ticket)):
        dig_lst2_part.append(int(ticket[digit]))

    if sum(dig_lst1_part) == sum((dig_lst2_part)):
        print(f'{ticket} -> yes')
    else:
        print(f'{ticket} -> no')

ticket = input("Введите номер вашего билета: ")
if len(ticket) != 6:
    print("!!! ALARM !!!\nОшибка 666: наши билеты содержат только 6 цифар")
else:
    check_luck(ticket)
