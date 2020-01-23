def check_brackets(brackets) -> str:
    i = 0
    j = 0
    stack = str()
    stack_check = str()

    for letter in brackets:
        i += 1

        if letter not in '()[]{}':
            continue

        if letter in '([{':
            stack += letter
        else:
            if len(stack) == 0:
                return str(i)

            if not ((stack[-1] == '(' and letter == ')') or
                    (stack[-1] == '[' and letter == ']') or
                    (stack[-1] == '{' and letter == '}')):
                return str(i)
            else:
                stack = stack[0:-1]

    if len(stack) == 0:
        return 'Success'
    else:
        if stack[-1] in '([{':
            for letter in brackets:
                j += 1

                if letter in '([{':
                    stack_check += letter

                if ((stack_check[-1] == '(' and letter == ')') or
                    (stack_check[-1] == '[' and letter == ']') or
                    (stack_check[-1] == '{' and letter == '}')):
                    stack_check = stack_check[0:-1]

                if stack == stack_check:
                    break

            return str(j)
        else:
            return str(i)


def get_source():
    brackets = str(input())
    print(check_brackets(brackets))


if __name__ == '__main__':
    get_source()
