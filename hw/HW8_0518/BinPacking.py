if __name__ == '__main__':
    len_of_num_list = int(input())
    num_list = list(map(float, input().split(' ')))
    bin_list = []

    # situ 1
    for num in num_list:
        #if bin_list == []:
        #    bin_list.append(num)

        puted_flag = False
        for i in range(len(bin_list)):
            if bin_list[i]+num <= 1.0:
                bin_list[i] += num
                puted_flag = True
                break

        if puted_flag == False:
            bin_list.append(num)

        #print('num, bin_list:', num, bin_list)
    print(len(bin_list))