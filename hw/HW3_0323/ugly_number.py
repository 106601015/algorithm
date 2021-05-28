def create_ugly_list(upper_limit):
    ugly_list = [1]
    for i in range(2, upper_limit):
        num = i
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        if num == 1:
            ugly_list.append(i)
    return ugly_list

if __name__ == '__main__':
    num_of_input = int(input())
    upper_limit = 1000
    ugly_list = create_ugly_list(upper_limit)
    for i in range(num_of_input):
        input_index = int(input())
        # if out of range
        while len(ugly_list) < input_index:
            upper_limit *= 10
            ugly_list = create_ugly_list(upper_limit)
        print(str(ugly_list[input_index-1]))