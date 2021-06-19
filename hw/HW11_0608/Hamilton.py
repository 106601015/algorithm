# graph node
class Node():
    def __init__(self, num):
        self.num = num
        self.connect_node_list = []
    def __call__(self, num):
        self.num = num
        self.connect_node_list = []
    def append_connect_node(self, node):
        self.connect_node_list.append(node)

if __name__ == '__main__':
    num_of_cases = int(input())
    for case_i in range(num_of_cases):
        num_list = []
        node_list = []
        num_of_edges = int(input())
        # create num_list + node_list
        for edge_i in range(num_of_edges):
            input_str = input()
            n1, n2 = input_str[1], input_str[3]
            n1, n2 = int(n1), int(n2)
            if n1 not in num_list:
                num_list.append(n1)
                node_list.append(Node(n1))
            if n2 not in num_list:
                num_list.append(n2)
                node_list.append(Node(n2))

            node_list[num_list.index(n1)].append_connect_node(node_list[num_list.index(n2)])
            node_list[num_list.index(n2)].append_connect_node(node_list[num_list.index(n1)])

        # test
        #for i in range(len(num_list)):
        #    print(num_list[i], node_list[i].connect_node_list[0].num)

        # dfs
        connect_node_list_stack = []
        hamilton_circuit = []
        hamilton_circuit.append(node_list[0])
        while True:
            if len(hamilton_circuit) == len(node_list) and hamilton_circuit[0] in hamilton_circuit[-1].connect_node_list: # if hamilton circuit done
                print('True')
                break

            new_list = hamilton_circuit[-1].connect_node_list[:] # call by value, don't change connect_node_list!
            connect_node_list_stack.append(new_list)

            #print('->', connect_node_list_stack)
            while connect_node_list_stack[-1] == []: # if there are no neighbors
                connect_node_list_stack.pop()
                hamilton_circuit.pop()
            if hamilton_circuit == []: # if dfs no found
                print('False')
                break
            if_break_flag = False
            while connect_node_list_stack[-1][-1] in hamilton_circuit: # if node is already in circuit
                connect_node_list_stack[-1].pop()
                while connect_node_list_stack[-1] == []: # if there are no neighbors
                    connect_node_list_stack.pop()
                    hamilton_circuit.pop()
                    if hamilton_circuit == []: # if dfs no found
                        print('False')
                        if_break_flag = True
                        break
                if if_break_flag:
                    break
            if if_break_flag:
                break
            hamilton_circuit.append(connect_node_list_stack[-1].pop()) # if connect_node_list_stack[-1][-1] not in circuit

            #for node in hamilton_circuit:
            #    print('-->', node.num)
        del num_list
        del node_list