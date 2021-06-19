# puzzle node, record puzzle_map
class Node():
    def __init__(self, puzzle_map):
        self.puzzle_map = puzzle_map
        self.zero_location = None
        #self.childrens = [] #<-- we don't need this anymore ;)
        self.get_zero_location()
    # find 0 location
    def get_zero_location(self):
        for i in range(3):
            if 0 in self.puzzle_map[i]:
                self.zero_location = [self.puzzle_map[i].index(0), i]

    # print puzzle map
    def show_puzzle_map(self):
        for i in range(3):
            output_str = ''
            for num in self.puzzle_map[i]:
                output_str += str(num)+' '
            print(output_str[:-1])

class BFS_Tree():
    def __init__(self, root_node):
        self.root_node = root_node                                              # set root node
        self.bfs_queue = [self.root_node]                                       # implies BFS queue
    def create_bfs_tree(self, target_node):
        while self.bfs_queue[0].puzzle_map != target_node.puzzle_map:           # if not target -> loop
            self.bfs_queue[0].show_puzzle_map()                                 # print puzzle_map
            poped_node = self.bfs_queue.pop(0)                                  # queue pop
            x, y = poped_node.zero_location[0], poped_node.zero_location[1]     # 0 location

            if y > 0:                                                           # if 0 can move up
                puzzle_map = [[], [], []]                                       # init puzzle_map
                for i in range(3):
                    for j in range(3):
                        puzzle_map[i].append(poped_node.puzzle_map[i][j])       # for call by value
                puzzle_map[y][x] = puzzle_map[y-1][x]                           # 0 <- num
                puzzle_map[y-1][x] = 0                                          # num <- 0
                self.bfs_queue.append(Node(puzzle_map))                         # push to queue
            if x < 2:                                                           # if 0 can move right
                puzzle_map = [[], [], []]                                       # init puzzle_map
                for i in range(3):
                    for j in range(3):
                        puzzle_map[i].append(poped_node.puzzle_map[i][j])       # for call by value
                puzzle_map[y][x] = puzzle_map[y][x+1]                           # 0 <- num
                puzzle_map[y][x+1] = 0                                          # num <- 0
                self.bfs_queue.append(Node(puzzle_map))                         # push to queue
            if y < 2:                                                           # if 0 can move down
                puzzle_map = [[], [], []]                                       # init puzzle_map
                for i in range(3):
                    for j in range(3):
                        puzzle_map[i].append(poped_node.puzzle_map[i][j])       # for call by value
                puzzle_map[y][x] = puzzle_map[y+1][x]                           # 0 <- num
                puzzle_map[y+1][x] = 0                                          # num <- 0
                self.bfs_queue.append(Node(puzzle_map))                         # push to queue
            if x > 0:                                                           # if 0 can move left
                puzzle_map = [[], [], []]                                       # init puzzle_map
                for i in range(3):
                    for j in range(3):
                        puzzle_map[i].append(poped_node.puzzle_map[i][j])       # for call by value
                puzzle_map[y][x] = puzzle_map[y][x-1]                           # 0 <- num
                puzzle_map[y][x-1] = 0                                          # num <- 0
                self.bfs_queue.append(Node(puzzle_map))                         # push to queue
        target_node.show_puzzle_map()                                           # out while, show last time


if __name__ == '__main__':
    # init input_puzzle_map and target_puzzle_map
    input_puzzle_map, target_puzzle_map = [], []
    for i in range(3):
        input_puzzle_map.append(list(map(int, input().split(' '))))
    for i in range(3):
        target_puzzle_map.append(list(map(int, input().split(' '))))

    root_node = Node(input_puzzle_map)
    target_node = Node(target_puzzle_map)
    tree = BFS_Tree(root_node)
    tree.create_bfs_tree(target_node)