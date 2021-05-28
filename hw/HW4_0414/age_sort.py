if __name__ == '__main__':
    while True:
        num_of_input = int(input())
        if num_of_input == 0:
            break

        num_list = list(map(int, input().split()))
        num_list.sort()

        num_str = ''
        for num in num_list:
            num_str += str(num)+' '
        #print(num_str[:-1])
        print(num_str)