import sys


def collect_max(straight_line, reverse_line, frame, count_of_elements):
    result = list()
    if frame == 0:
        for i in range(0, (count_of_elements - frame)):
            result.append(max(reverse_line[i], straight_line[i + max(frame, 1) - 1]))
    else:
        for i in range(0, (count_of_elements - frame)):
            result.append(max(reverse_line[i], straight_line[i + max(frame, 1)]))

    print(' '.join([str(elem) for elem in result]))


def get_lines(original_line, frame, count_of_elements):
    frame -= 1
    i = 0
    j = count_of_elements - 2
    reverse_line = [0 for i in range(count_of_elements)]
    straight_line = [0 for i in range(count_of_elements)]

    while i < count_of_elements:
        if frame != 0 and i % frame:
            straight_line[i] = max(original_line[i], straight_line[i - 1])
        else:
            straight_line[i] = original_line[i]
        i += 1

    reverse_line[-1] = original_line[-1]

    while j >= 0:
        if frame != 0 and (j + 1) % frame:
            reverse_line[j] = max(original_line[j], reverse_line[j + 1])
        else:
            reverse_line[j] = original_line[j]
        j -= 1

    collect_max(straight_line, reverse_line, frame, count_of_elements)


def get_source():
    count_of_elements = int(input())
    original_line = list(map(int, str(input()).split(' ')))
    width_of_frame = int(input())
    if len(original_line) <= width_of_frame:
        print(max(original_line))
        sys.exit(0)
    get_lines(original_line, width_of_frame, count_of_elements)


if __name__ == '__main__':
    get_source()
