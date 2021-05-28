if __name__ == '__main__':
    num_of_cases = int(input())
    for case_i in range(num_of_cases):
        con = 0
        num_of_str = int(input())
        for buf2 in range(num_of_str):
            s = input()
            dic = {}

            for c in s:
                if dic.get(c) == None:
                    dic[c] = 0
                dic[c] += 1

            dic_set = set(dic.values())
            if len(dic_set) == len(dic) and len(dic) >= 2:
                con += 1
        print('Case {}: {}'.format(str(case_i+1), str(con)))