import queue


def printer(log):
    for r in log:
        print(r)


def init_queue(processors):
    proc = queue.PriorityQueue(processors)
    free_proc = queue.PriorityQueue(processors)

    for p in range(processors):
        free_proc.put(p)

    return proc, free_proc


def add_queue(proc, free_proc, task_time):
    process_memory = dict()

    if not free_proc.empty():
        processor = free_proc.get()
        time = process_memory[processor] if processor in process_memory else 0
    else:
        time, processor = proc.get()

    if task_time == 0:
        free_proc.put(processor)
        process_memory[processor] = time
    else:
        proc.put((time + task_time, processor))

    return str(str(processor) + ' ' + str(time))


def get_source():
    processors, tasks = map(int, str(input()).split(' '))
    times = list(map(int, str(input()).split(' ')))
    log = list()
    proc, free_proc = init_queue(processors)

    for time in times:
        log.append(add_queue(proc, free_proc, time))

    printer(log)


if __name__ == '__main__':
    get_source()
