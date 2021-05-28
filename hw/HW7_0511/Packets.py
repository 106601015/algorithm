import math

if __name__ == '__main__':
    while True:
        num_list = list(map(int, input().split(' ')))
        if num_list == [0, 0, 0, 0, 0, 0]:
            break

        boxs = 0
        # 6*6
        boxs += num_list[5]
        # 5*5
        boxs += num_list[4]
        if num_list[0] <= 11*num_list[4]:
            num_list[0] = 0
        else:
            num_list[0] -= 11*num_list[4]
        # 4*4
        boxs += num_list[3]
        if num_list[1] <= 5*num_list[3]:
            num_list[1] = 0
        else:
            num_list[1] -= 5*num_list[3]
        # 3*3
        boxs += int(num_list[2]/4)
        num_list[2] -= int(num_list[2]/4)*4
        # loss 3*3, 2*2 and 1*1
        buf = (num_list[2]*9 + num_list[1]*4 + num_list[0])/36
        if buf % 1 == 0:
            boxs += int(buf)
        else:
            boxs += int(buf)+1

        print(boxs)