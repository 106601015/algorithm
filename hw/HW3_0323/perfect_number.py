def find_perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        return True
    else:
        return False

if __name__ == '__main__':
    num_of_input = int(input())
    input_list = list(map(int, input().split(' ')))
    output_str = ''
    for input_num in input_list:
        if(find_perfect(input_num)):
            output_str += str(input_num) + ' '
    print(output_str[:-1])
