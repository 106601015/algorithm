if __name__ == '__main__':
    num_of_cases = int(input())
    for case_i in range(num_of_cases):
        num_list = list(map(int, input().split(' ')))
        k = int(input())
        num_list.sort()
        print(num_list[k-1])