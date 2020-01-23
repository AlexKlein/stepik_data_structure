import sys


def get_hash_id(string, table_width, power):
    hash_id = 0

    for i, letter in enumerate(string):
        hash_id += ord(letter) * power[i]

    return (hash_id % 1000000007) % table_width


def add(hash_table, hash_id, string) -> list:

    if string not in hash_table[hash_id]:
        hash_table[hash_id].insert(0, string)

    return hash_table


def remove(hash_table, hash_id, string) -> list:
    try:
        hash_table[hash_id].remove(string)
    except ValueError as e:
        pass

    return hash_table


def find(hash_table, hash_id, string):

    if string not in hash_table[hash_id]:
        print('no')
    else:
        print('yes')


def check(hash_table, hash_id):
    if len(hash_table[hash_id]) > 0:
        print(' '.join(hash_table[hash_id]))
    else:
        print('')


def get_source():
    power = [263 ** x for x in range(15)]
    table_width = int(input())
    hash_table = [list() for i in range(table_width)]
    count_of_queries = int(input())
    for line in sys.stdin:
        if line.find('check ') >= 0:
            func, hash_id = map(str, str(line.replace('\n', '').lstrip()).split(' '))
            hash_id = int(hash_id)
            check(hash_table, hash_id)
        else:
            func, string = map(str, str(line.replace('\n', '')).split(' '))

            if func == 'add':
                hash_table = add(hash_table, get_hash_id(string, table_width, power), string)
            elif func == 'del':
                hash_table = remove(hash_table, get_hash_id(string, table_width, power), string)
            elif func == 'find':
                find(hash_table, get_hash_id(string, table_width, power), string)


if __name__ == '__main__':
    get_source()
