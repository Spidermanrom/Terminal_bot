from classes import Address_book, Contact, Birthday

import pathlib
import pickle

cache = [Address_book()]

# Функція декоратор для обробки помилок
def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except IndexError:
            return "IndexError"
        except ValueError:
            return "ValueError"
        except KeyError:
            return "KeyError"
        except TypeError:
            return "TypeError"
        except ArithmeticError:
            return 'ArithmeticError'
    return wrap


def greeting():
    return "Вітаю! Ласкаво просимо до вашого персонального помічника."

def add_contact():
    pass

def change_number():
    pass

def phone_output():
    pass

def show_all_contacts():
    pass

def show_all():
    commands = [['Command', 'Parameters', 'Description'],
                   ['all', '', 'list all information about users'],
                   ['add', '[Name]', 'create new user [Name] in adress book'],
                   ['edit', '[Contact_id] [new_Name]', 'edit name of [Contact_id] to [new_Name]'],
                   ['del', '[Contact_id]', 'remove user [Contact_id] from adress book'],
                   ['add-phone', '[Contact_id] [Phone]', 'add to user [Contact_id] a [Phone]'],
                   ['edit-phone', '[Contact_id] [Phone] [new_Phone]', 'replace for user [Contact_id] a [Phone] by [new_Phone]'],
                   ['del-phone', '[Name] [Phone]', 'remove phone [Phone] from user [Name]'],
                   ['add-email', '[Contact_id] [Email]', 'add to user [Contact_id] an [Email]'],
                   ['edit-email', '[Contact_id] [Email] [new_Email]', 'replace for user [Contact_id] an [Email] by [new_Email]'],
                   ['del-email', '[Contact_id] [Email]', 'remove email [Email] from user [Contact_id]'],
                   ['address', '[Contact_id] [Address]', 'set for user [Name] an address [Address]'],
                   ['del-address', '[Contact_id]', 'remove address from [Contact_id]'],
                   ['birthday', '[Contact_id] [Birthday]', 'set for user [Contact_id] a birthday at [Birthday]'],
                   ['del-birthday', '[Contact_id]', 'remove birthday from [Contact_id]'],
                   ['find', '[search]', 'list [search] data in Name, Phones, Address, Emails, Birthdays. [search] must be 2 symbols min'],
                   ['next-birthdays', '[int]', 'shows upcoming birthdays if exist in period from today till [int] days'],
                   ['note', '', 'Add a note to Note Book'],
                   ['all-notes', '', 'list all notes'],
                   ['edit-note', '[Note_id] [Note]', 'edit text of [Note_id] Note'],
                   ['del-note', '[Note_id]', 'Remove [Note_id] note from Note Book'],
                   ['add-tag', '[Note_id] [Tag]', 'add [Tag] to note [Note_id]'],
                   ['del-tag', '[Note_id] [Tag]', 'remove [Tag] from note [Note_id]'],
                   ['find-notes', '[searchstring]', 'list all Notes with [searchstring] data in note and tags.[searchstring] must be 2 symbols minimum'],
                   ['find-tags', '[searchstring]', 'list all Notes with [searchstring] data in tags.[searchstring] must be 2 symbols minimum'],
                   ['sort-tag', '', 'list all Notes sorted by number of tags'],
                   ['close, exit', '', 'exit the bot'],
                   ['help', '', 'list all bot commands']]
    dashes = "{0:<14} + {1:<32} + {2:^12} \n".format("-" * 14, "-" * 32, "-" * 12)
    help_string = ''

    for i in commands:
        help_string += f'{i[0]:^14} | {i[1]:^32} | {i[2]:^12} \n'
        help_string += dashes
    print(help_string)

def delete():
    pass

def add_birthday(book: Address_book, args: list):
    if len(args) == 2:
        try:
            if int(args[0]) in book.data:
                rec = book.data[int(args[0])]
                rec.birthday = Birthday(args[1])
                print('Birthday added sucessfully.')
            else:
                print(f'Contact id {args[0]} not found')
        except ValueError:
            print('Error: Date format must be: DD.MM.YYYY')
    else:
        print('Error: Invalid command format.')

def days_to_birthday():
    pass

def note():
    pass

def add_note():
    pass

def change_note():
    pass

def note_output():
    pass

def delete_note():
    pass

def show_all_notes():
    pass

def search_note():
    pass

def tag():
    pass

def add_tag():
    pass

def delete_tag():
    pass

def about():
    pass

def sorting():
    pass

# Функція для запису кешу в окремий файл для зберігання данних
def exit(data):
    # Якщо кеш пустий та окремий файл для зберігання існує тоді файл буде видалено
    if not cache and pathlib.Path('cache.bin').exists():
        pathlib.Path('cache.bin').unlink()
        return None
    with open('cache.bin', 'wb') as file:
        pickle.dump(cache, file)

# Функія для відновлення кешу при повторному виклику програми
def return_cache():
    with open('cache.bin', 'rb') as file:
        global cache
        cache = pickle.load(file)

# Словник ключ = Функція, значення= Ключові слова для запуску функцій
COMMANDS = {
    greeting: 'hello',
    add_contact: 'add',
    change_number: 'change',
    phone_output: 'phone',
    show_all: 'show all',
    exit: ['exit', 'good bye', 'close'],
    delete: 'delete',
    about: 'about',
    add_birthday: 'birthday',
    days_to_birthday: 'days to birthday',
    add_note: 'note',
    delete_note: 'del note',
    show_all_notes: 'show all notes',
    search_note: 'snote',
    add_tag: 'tag',
    delete_tag: 'del tag',
    sorting: 'sorting'
}

def commands(data):
    pass

def main():
    # Якщо раніше використовувалася програма та було створено кеш: його буде відновлено
    if pathlib.Path('cache.bin').exists():
        return_cache()
    # Цикл для тривалої роботи програми
    while True:
        # Отримання даних від користувачаa
        user_input = input('>>>')
        if user_input:
            func, data = commands(user_input)
        if func == None:
            continue
        elif func == exit:
            # Вихід з програми та запис кешу в окремий файл
            func(data)
            print('Good bye')
            break
        else:
            # Запуск команд
            result = func(data)
            print(result)


if __name__ == '__main__':
    main()
