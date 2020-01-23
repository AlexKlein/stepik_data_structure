def get_hash_id(string):
    return sum(ord(x) for x in list(string))


def search_substring(string, substring) -> list:
    matches = list()

    len_str = len(string)
    len_sub_str = len(substring)

    base_hash = get_hash_id(string[:len_sub_str:])
    sub_str_hash = get_hash_id(substring)

    for i in range(0, len_str - len_sub_str + 1):
        next_i = len_sub_str + i

        prev = 0 if i == 0 else ord(string[i - 1])
        last = 0 if i == 0 else ord(string[next_i - 1])

        base_hash = base_hash - prev + last

        if base_hash == sub_str_hash and substring == string[i:next_i]:
            matches.append(str(i))

    return matches


def get_source():
    substring = str(input())
    string = str(input())
    print(' '.join(search_substring(string, substring)))


if __name__ == '__main__':
    get_source()
