book_dict = {}

def read_phonebook():
    with open('Phonebook.txt', 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for i in data:
            print(i)
    return data


def add_contact(name, number):
    with open('Phonebook.txt', 'a', encoding='UTF-8') as file:
        book_dict[name] = number
        file.write(f'{name}: {number}\n')
    print(f'Контакт {name} с номером {number} успешно добавлен в телефонный справочник!')
    return read_phonebook()


def find_contact(name):
    with open('Phonebook.txt', 'r', encoding="UTF-8") as file:
        for i in file.readlines():
            if i:
                key,val = i.strip().split(': ')
                book_dict[key] = val
        for i in book_dict.keys():
            if i == name:
                return f'{i} - {book_dict[i]}'
        else:
            print("Такого контакта нет. Записать его в справочник? [y \ n]")
            check = input()
            if check == 'y':
                add_contact(name, input("Введите номер: "))
            else:
                return read_phonebook()


def change_contact(name):
    with open('Phonebook.txt', 'rt', encoding='UTF-8') as data:
        file = data.read()
        if name in file:
            print("Перезаписать имя или номер? [и \ н] ")
            check_rewrite = input()
            if check_rewrite == 'и':
                file = file.replace(name, input("Введите новое имя контакта: "))
                with open('Phonebook.txt', 'wt', encoding="UTF-8") as file1:
                    file1.write(file)
                    print("Контакт успешно изменен!")
            else:
                with open('Phonebook.txt', 'rt', encoding='UTF-8') as data2:
                    file3 = data2.readlines()
                    for i in file3:
                        key, val = i.strip().split(': ')
                        book_dict[key] = val
                    book_dict[name] = input("Введите новый номер контакта: ")

                    data1 = ''
                    for key, val in book_dict.items():
                        if i:
                            data1 += f'{key}: {val}\n'


                with open('Phonebook.txt', 'wt', encoding="UTF-8") as file1:
                    file1.write(data1)
                    print("Контакт успешно изменен!")
            return read_phonebook()
        else:
            print("Такого контакта нет. Записать его в справочник? [y \ n]")
            check = input()
            if check == 'y':
                add_contact(name, input("Введите номер: "))
            else:
                return read_phonebook()


def delete_contact(name):
    with open('Phonebook.txt', 'rt', encoding="UTF-8") as file:
        for i in file.readlines():
            if i:
                key, val = i.strip().split(': ')
                book_dict[key] = val

        if name in book_dict:
            del book_dict[name]
            data = ''
            for key, val in book_dict.items():
                data += f'{key}: {val}\n'
            print("Контакт успешно удален!")
        else:
            return "Контакт не найден"

    with open('Phonebook.txt', 'wt', encoding="UTF-8") as file1:
        file1.write(data)
        print("Контакт успешно удален!")
    return read_phonebook()


def check_action(num):
    match num:
        case 1:
            read_phonebook()
            check_action(int(input(choice_func)))
        case 2:
            add_contact(input('Как зовут контакт?\n').upper(), input('Какой номер?\n'))
            check_action(int(input(choice_func)))
        case 3:
            find_contact(input("Введите имя: ").upper())
            check_action(int(input(choice_func)))
        case 4:
            read_phonebook()
            change_contact(input("Какой контакт изменить?\n").upper())
            check_action(int(input(choice_func)))
        case 5:
            read_phonebook()
            delete_contact(input("Какой контакт удалить?  ").upper())
            check_action(int(input(choice_func)))
        case 6:
            exit()

choice_func = "\n\n\nВыбрать действие:\nПоказать все контакты - 1. \nДобавить новый контакт - 2.\nУдалить контакт - 5.\nНайти контакт - 3.\nИзменить контакт - 4. \nВыйти - 6.\n "
check_action(int(input("К вашим услугам телефонный справочник.\nПоказать все контакты - 1. \nДобавить новый контакт - 2.\nУдалить контакт - 5.\nНайти контакт - 3.\nИзменить контакт - 4. \nВыйти - 6.\n ")))
