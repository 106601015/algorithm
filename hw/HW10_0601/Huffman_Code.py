# Huffman tree node
class Node():
    def __init__(self, num_str=None, frequency=None):
        self.num_str = num_str
        self.frequency = frequency
        self.left = None
        self.right = None
    def set_left(self, left_node):
        self.left = left_node
    def set_right(self, right_node):
        self.right = right_node
# Huffman tree
class tree():
    # create a Huffman tree, set root
    def __init__(self, node_list):
        while len(node_list) != 1:
            father = Node(
                num_str=node_list[0].num_str + node_list[1].num_str,
                frequency=node_list[0].frequency + node_list[1].frequency
            )
            father.set_left(node_list[0])
            father.set_right(node_list[1])
            node_list = node_list[2:]
            node_list.append(father)
            node_list.sort(key=lambda node:node.frequency)
        self.root = node_list[0]
        #print('----> root:', self.root.num_str, self.root.frequency)
    # encode all tree(recursive call)
    def encode(self):
        code = ''
        self.code_recoder_dict = {}
        self.encode_single_node(self.root, code)
        return self.code_recoder_dict
    def encode_single_node(self, node, code):
        # if only one number input
        if self.root.left == None and self.root.right == None:
            self.code_recoder_dict[self.root.num_str] = '0'
        # if basic node
        if node.left == None and node.right == None:
            self.code_recoder_dict[node.num_str] = code
        else:
            self.encode_single_node(node.left, code+'0')
            self.encode_single_node(node.right, code+'1')


if __name__ == '__main__':
    input_str = input()
    frequency_dict = {}
    for ch in input_str:
        frequency = frequency_dict.get(ch, -1)
        if frequency == -1:
            frequency_dict[ch] = 1
        else:
            frequency_dict[ch] += 1
    sorted_frequency_list = sorted(frequency_dict.items(), key=lambda x:x[1])
    node_list = [Node(piece[0], piece[1]) for piece in sorted_frequency_list]
    new_tree = tree(node_list)
    code_recoder_dict = new_tree.encode()

    sorted_code_recoder_list = sorted(code_recoder_dict.items(), key=lambda x:int(x[1]))
    for i in range(len(sorted_code_recoder_list)):
        print('{}:{}'.format(sorted_code_recoder_list[i][0], sorted_code_recoder_list[i][1]))