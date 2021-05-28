if __name__ == '__main__':
    num_of_cases = int(input())
    for buf in range(num_of_cases):
        num_of_data = int(input())

        # create sorted positive_list/negative_list
        positive_list, negative_list = [], []
        for buff in range(num_of_data):
            data = int(input())
            if data > 0:
                positive_list.append(data)
            else:
                negative_list.append(data)
        positive_list.sort()
        negative_list.sort(reverse = True)

        # init p_i/n_i/height/area and +/- list and p_n_flag(+ or -)
        p_i, n_i, height, area = 0, 0, 0, 0
        if positive_list[p_i] < abs(negative_list[n_i]):
            area = positive_list[p_i]
            p_i += 1
            height += 1
            p_n_flag = False
        else:
            area = abs(negative_list[n_i])
            n_i += 1
            height += 1
            p_n_flag = True

        # crossed check +/- list until (index over + your turn)
        while True:
            #print('p_i, n_i, height, area:', p_i, n_i, height, area)
            if p_i == len(positive_list) and p_n_flag == True:
                break
            if n_i == len(negative_list) and p_n_flag == False:
                break

            if p_n_flag:
                if positive_list[p_i] > area:
                    area = positive_list[p_i]
                    height += 1
                    p_n_flag = False
                p_i += 1
            else:
                if abs(negative_list[n_i]) > area:
                    area = abs(negative_list[n_i])
                    height += 1
                    p_n_flag = True
                n_i += 1

        print(height)