if __name__ == '__main__':
    num_of_cases = int(input())
    for buf in range(num_of_cases):
        num_of_input = int(input())
        num_list = list(map(int, input().split(' ')))
        avg = sum(num_list) / len(num_list)

        total_positive_move = 0
        for num in num_list:
            positive_move = num-avg
            if positive_move > 0:
                total_positive_move += positive_move
        print(int(total_positive_move))