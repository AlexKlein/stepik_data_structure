def get_max_height(height_dict):
    max_height = 0

    for height in height_dict:
        if height_dict.get(height) > max_height:
            max_height = height_dict.get(height)

    print(max_height)


def get_nodes_height(count_of_nodes, adjacency_list):
    height = 1
    height_dict = dict()
    root = adjacency_list.get('-1')
    height_dict.update({root: height})
    queue = adjacency_list.get(root)
    queue_next = ''
    while len(height_dict) < count_of_nodes:
        height += 1

        for elem in queue.split(','):
            height_dict.update({elem: height})
            if queue_next == '':
                if adjacency_list.get(elem):
                    queue_next = str(adjacency_list.get(elem))
            else:
                if adjacency_list.get(elem):
                    queue_next = queue_next + ',' + adjacency_list.get(elem)

        queue = queue_next
        queue_next = ''

    get_max_height(height_dict)


def adjacency_list_collect(count_of_nodes, list_of_parent_nodes):
    adjacency_list = dict()
    j = 0

    for node in list_of_parent_nodes.split():
        if adjacency_list.get(node):
            adjacency_list.update({str(node): adjacency_list.get(node) + ',' + str(j)})
        else:
            adjacency_list[str(node)] = str(j)
        j += 1

    get_nodes_height(count_of_nodes, adjacency_list)


def get_source():
    count_of_nodes = int(input())
    list_of_parent_nodes = str(input())
    adjacency_list_collect(count_of_nodes, list_of_parent_nodes)


if __name__ == '__main__':
    get_source()
