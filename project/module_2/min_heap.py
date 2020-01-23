def get_parent(i) -> int:
    if (i == 0) or (i == 1) or (i == 2):
        return 0
    elif i % 2 == 0:
        return (i - 1) // 2
    else:
        return i // 2


def get_left_child(i) -> int:
    return (2 * i) + 1


def get_right_child(i) -> int:
    return (2 * i) + 2


def get_root() -> int:
    return 0


def sift_down(i, heap, result_log) -> list:
    j = i
    parent_idx = get_parent(j)

    while parent_idx > 0 or j > 0:
        parent = heap[parent_idx]
        current = heap[j]

        if parent > current:
            heap[parent_idx] = current
            heap[j] = parent
            result_log.append(str(parent_idx) + ' ' + str(j))

        j = parent_idx
        parent_idx = get_parent(j)

    return heap


def sift_up(i, size, heap, result_log) -> list:
    current = heap[i]
    left_idx = get_left_child(i)
    right_idx = get_right_child(i)

    while left_idx < size:
        min_idx = left_idx

        if right_idx < size and heap[right_idx] < heap[min_idx]:
            min_idx = right_idx

        if current <= heap[min_idx]:
            break

        heap[i], heap[min_idx] = heap[min_idx], heap[i]
        result_log.append(str(i) + ' ' + str(min_idx))
        i = min_idx
        left_idx = get_left_child(i)
        right_idx = get_right_child(i)

    return heap


def get_source() -> list:
    result_log = list()
    size = int(input())
    base_size = size // 2
    unsorted_heap = list(map(int, str(input()).split(' ')))

    for i in range(base_size, - 1, -1):
        sift_up(i, size, unsorted_heap, result_log)

    return result_log


if __name__ == '__main__':
    result = get_source()
    print(len(result))

    for r in result:
        print(r)
