if __name__ == '__main__':
    while True:
        num_of_cases = int(input())
        if num_of_cases == 0:
            break

        biggest_case, biggest_edge = -1, 0
        for case_i in range(num_of_cases):
            input_list = list(map(int, input().split(' ')))
            edge_proportion = input_list[0]/input_list[1]
            if edge_proportion > 4.0:
                edge = input_list[1]
            elif edge_proportion < 0.25:
                edge = input_list[0]
            else:
                edge = min(input_list[0], input_list[1])/2

            if edge > biggest_edge:
                biggest_edge = edge
                biggest_case = case_i
        print(biggest_case+1)
