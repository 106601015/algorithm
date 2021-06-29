class Graph():
    def __init__(self, n):
        self.alpha_list = []
        self.d = []
        self.p = []
        for i in range(n):
            self.d.append([])
            self.p.append([])
            for j in range(n):
                if i == j:
                    self.d[i].append(0)
                else:
                    self.d[i].append(999)
                self.p[i].append('None')
    def append_alpha(self, alpha):
        self.alpha_list.append(alpha)
    def append_path(self, begin_alpha, end_alpha, cost):
        assert begin_alpha in self.alpha_list
        assert end_alpha in self.alpha_list
        assert begin_alpha != end_alpha
        begin_index = self.alpha_list.index(begin_alpha)
        end_index = self.alpha_list.index(end_alpha)
        self.d[begin_index][end_index] = cost
        self.p[begin_index][end_index] = begin_alpha
    def sort_all(self):
        n = len(self.alpha_list)
        self.sorted_alpha_list = sorted(self.alpha_list)
        self.sorted_d, self.sorted_p = [], []
        for i in range(n):
            self.sorted_d.append(self.d[i][:])
            self.sorted_p.append(self.p[i][:])
        for i in range(n):
            for j in range(n):
                self.sorted_d[i][j] = self.d[self.alpha_list.index(self.sorted_alpha_list[i])][self.alpha_list.index(self.sorted_alpha_list[j])]
                self.sorted_p[i][j] = self.p[self.alpha_list.index(self.sorted_alpha_list[i])][self.alpha_list.index(self.sorted_alpha_list[j])]
        self.alpha_list = self.sorted_alpha_list
        self.d = self.sorted_d
        self.p = self.sorted_p
    def floyd_warshall(self):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.d[i][k] == 999 or self.d[k][j] == 999:
                        pass
                    else:
                        new_cost = self.d[i][k]+self.d[k][j]
                        if self.d[i][j] > new_cost or self.d[i][j] == 999:
                            self.d[i][j] = new_cost
                            self.p[i][j] = self.p[k][j]
        return self.d, self.p

if __name__ == '__main__':
    input_int_list = list(map(int, input().split(' ')))
    n, path_num = input_int_list[0], input_int_list[1]
    graph = Graph(n)

    for i in range(path_num):
        input_str = input()
        input_str_list = input_str.split(' ')
        begin_alpha, end_alpha, cost = input_str_list[0], input_str_list[1], int(input_str_list[2])
        if begin_alpha not in graph.alpha_list:
            graph.append_alpha(begin_alpha)
        if end_alpha not in graph.alpha_list:
            graph.append_alpha(end_alpha)
        graph.append_path(begin_alpha, end_alpha, cost)
    assert len(graph.alpha_list) == n
    graph.sort_all()
    d, p = graph.floyd_warshall()
    #print(d)

    for i in range(n):
        output_str = ''
        for j in range(n):
            if d[i][j] == 999:
                output_str += 'INF '
            else:
                output_str += str(d[i][j]) + ' '
        print(output_str[:-1])



'''
5 9
a b 3
a c 8
b d 1
a e -4
c b 4
b e 7
d c -5
d a 2
e d 6
'''
'''
5 9
b e 7
d c -5
a b 3
a c 8
b d 1
a e -4
c b 4
d a 2
e d 6
'''
'''
5 7
A B 6
A C 5
A D 11
A E 16
B C -3
C D -2
D E 2
'''