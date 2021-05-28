if __name__ == '__main__':
    c = int(input())
    input_list = []
    for i in range(c):
        input_list.append(int(input()))
        input_list.sort()
        if len(input_list) % 2 == 1:
            print(str(input_list[int(len(input_list)/2)]))
        else:
            print(str(int((input_list[int(len(input_list)/2)-1] + input_list[int(len(input_list)/2)])/2)))