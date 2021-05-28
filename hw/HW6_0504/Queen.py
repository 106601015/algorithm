if __name__ == '__main__':
    while True:
        # get input to coordinate, init flag
        num_list = list(map(int, input().split(' ')))
        begin_coordinate, over_coordinate = num_list[:2], num_list[2:]
        yes_queen_can_flag = False

        # if any 0 in num_list -> break
        if 0 in num_list:
            break

        # check same row and column
        if begin_coordinate[0] == over_coordinate[0] or begin_coordinate[1] == over_coordinate[1]:
            yes_queen_can_flag = True
        # check bottom left to top right
        elif begin_coordinate[1] - begin_coordinate[0] == over_coordinate[1] - over_coordinate[0]:
            yes_queen_can_flag = True
        # check bottom right to top left
        elif begin_coordinate[1] + begin_coordinate[0] == over_coordinate[1] + over_coordinate[0]:
            yes_queen_can_flag = True

        # print
        if yes_queen_can_flag:
            print('True')
        else:
            print('False')