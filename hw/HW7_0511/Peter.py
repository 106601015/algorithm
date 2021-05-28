if __name__ == '__main__':
    num_of_cases = int(input())
    for buf in range(num_of_cases):
        num_list = list(map(int, input().split(' ')))
        k, n = num_list[0], num_list[1]

        total_n, tails = n, n
        while tails >= k:
            new_n = int(tails/k)
            total_n += new_n
            tails = tails % k + new_n
        print(total_n)