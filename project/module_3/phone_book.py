import sys


def add(phone_book, phone, name) -> list:
    phone_book[phone] = name
    return phone_book


def remove(phone_book, phone) -> list:
    phone_book[phone] = '0'
    return phone_book


def find(phone_book, phone):
    if phone_book[phone] == '0':
        print('not found')
    else:
        print(phone_book[phone])


def get_source():
    phone_book = ['0' for i in range(10000000)]
    count_of_elements = int(input())
    for line in sys.stdin:
        if line.find('add') >= 0:
            func, phone, name = map(str, str(line.replace('\n', '')).split(' '))
        else:
            func, phone = map(str, str(line.replace('\n', '')).split(' '))
        phone = int(phone)
        if func == 'add':
            phone_book = add(phone_book, phone, name)
        elif func == 'del':
            phone_book = remove(phone_book, phone)
        elif func == 'find':
            find(phone_book, phone)


if __name__ == '__main__':
    get_source()
