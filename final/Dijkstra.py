# graph node, record alpha + cost + pointed_node_list + pointed_node_cost_list
class Node():
    def __init__(self, alpha):
        self.alpha = alpha
        self.cost = 999
        self.pointed_node_list = []
        self.pointed_node_cost_list = []

class Graph():
    def __init__(self):
        self.node_list = []
    def append_node(self, node):
        self.node_list.append(node)
    def append_path(self, begin_alpha, end_alpha, cost):
        for i in range(len(self.node_list)):
            if self.node_list[i].alpha == begin_alpha:
                begin_node = self.node_list[i]
            if self.node_list[i].alpha == end_alpha:
                end_node = self.node_list[i]
        if end_node not in begin_node.pointed_node_list:
            begin_node.pointed_node_list.append(end_node)
            begin_node.pointed_node_cost_list.append(cost)

    def dijkstra_walk(self, source_alpha, target_alpha):
        walked_node_list = []
        BFS_node_queue = []

        for node in self.node_list:                 # init s cost = 0
            if node.alpha == source_alpha:
                node.cost = 0
                BFS_node_queue.append(node)

        while walked_node_list != self.node_list:   # walk around all nodes
            poped_node = BFS_node_queue.pop(0)
            walked_node_list.append(poped_node)

            for pointed_node in poped_node.pointed_node_list: # renew pointed_node cost
                new_cost = poped_node.cost + poped_node.pointed_node_cost_list[poped_node.pointed_node_list.index(pointed_node)]
                #print('=>', pointed_node.alpha, new_cost)
                if new_cost < pointed_node.cost:
                    #print('cost:', new_cost, pointed_node.cost)
                    pointed_node.cost = new_cost
                if pointed_node not in walked_node_list and pointed_node not in BFS_node_queue:
                    #print('input:', pointed_node.alpha)
                    BFS_node_queue.append(pointed_node)

        for node in self.node_list:
            if node.alpha == target_alpha:
                return node.cost


if __name__ == '__main__':
    input_str = input()
    source_alpha, target_alpha = input_str[0], input_str[2]
    inputed_alpha_list = []
    graph = Graph()

    path_num = int(input())
    for i in range(path_num):
        input_str_list = input().split(' ')
        begin_alpha, end_alpha, cost = input_str_list[0], input_str_list[1], int(input_str_list[2])
        if begin_alpha not in inputed_alpha_list:
            inputed_alpha_list.append(begin_alpha)
            graph.append_node(Node(begin_alpha))
        if end_alpha not in inputed_alpha_list:
            inputed_alpha_list.append(end_alpha)
            graph.append_node(Node(end_alpha))
        graph.append_path(begin_alpha, end_alpha, cost)

    shortest_cost = graph.dijkstra_walk(source_alpha, target_alpha)
    print(shortest_cost)