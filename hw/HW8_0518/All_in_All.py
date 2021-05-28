if __name__ == '__main__':
    num_of_cases = int(input())
    for buf in range(num_of_cases):
        s, t = input().split(' ')

        con = 0
        yes_flag = False
        for ch_t in t:
            if ch_t == s[con]:
                con += 1
            if con == len(s)-1:
                yes_flag = True
                break

        if yes_flag:
            print('Yes')
        else:
            print('No')