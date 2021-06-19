if __name__ == '__main__':
    num_of_cases = int(input())
    for case_i in range(num_of_cases):
        input_list = list(map(int, input().split(' ')))
        n, s = input_list[0], input_list[1]
        if n == 0 and s == 0:
            break
        denomination_list = list(map(int, input().split(' ')))
        denomination_list.sort(reverse=True)

        min_num = 9999
        for i in range(len(denomination_list)):
            num = 0
            remain_s = s
            for j in range(i, len(denomination_list)):
                single_num = remain_s//denomination_list[j]
                if single_num == 0:
                    continue
                remain_s -= single_num * denomination_list[j]
                num += single_num
                if remain_s == 0:
                    break
            if min_num >= num:
                min_num = num
        print(min_num)
