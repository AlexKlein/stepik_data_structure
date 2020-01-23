import sys


MAIN_STACK = list()
MAX_STACK = list()


def stack_push(value):
    global MAIN_STACK
    global MAX_STACK

    MAIN_STACK.append(value)
    if len(MAX_STACK) > 0:
        if MAX_STACK[-1] > value:
            MAX_STACK.append(MAX_STACK[-1])
        else:
            MAX_STACK.append(value)
    else:
        MAX_STACK.append(value)


def stack_pop():
    MAIN_STACK.pop()
    MAX_STACK.pop()


def stack_max():
    try:
        print(MAX_STACK[len(MAX_STACK) - 1])
    except IndexError:
        print(0)


def get_source():
    count_of_cmd = int(input())

    for line in sys.stdin:
        line = str(line).replace('\n', '')
        if str(line).find('pop') >= 0:
            stack_pop()
        elif str(line).find('max') >= 0:
            stack_max()
        elif str(line).find('push') >= 0:
            cmd, value = str(line).split(' ')
            stack_push(int(value))


if __name__ == '__main__':
    get_source()
