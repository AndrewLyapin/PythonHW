'''
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе
несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает
в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом
все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
    **Вывод:** Парам пам-пам
'''

lst_vowel = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
song = input("Введите вашу песню: ").split()


def str_to_list(song):
    song = [list(song[i]) for i in range(len(song))]
    return song


def count_in(song, lst_vowel):
    lst = [song[j].count(lst_vowel[b]) for j in range(len(song)) for b in range(len(lst_vowel))]
    return lst


def slice_lsts(lst, lst_vowel):
    slice_lst = [lst[x:len(lst_vowel)+x] for x in range(0, len(lst), len(lst_vowel))]
    return slice_lst


def sum_el_lsts(slice_lst):
    slice_lst = [sum(slice_lst[i]) for i in range(len(slice_lst))]
    return slice_lst


def check_eq(sum_el_lst):
    print("Парам пам-пам" if len(set(sum_el_lst)) == 1 else "Пам парам")

song = str_to_list(song)
lst_count = count_in(song, lst_vowel)
slice_lst = slice_lsts(lst_count, lst_vowel)
sum_el_lst = sum_el_lsts(slice_lst)
check_eq(sum_el_lst)

