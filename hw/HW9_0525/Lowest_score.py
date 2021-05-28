if __name__ == '__main__':
    num_of_cases = int(input())
    for case_i in range(num_of_cases):
        list_len = int(input())
        num_list = list(map(int, input().split(' ')))
        output_str = ''

        a_index, b_index = 0, 0
        for i in range(list_len):
            if num_list[i] > num_list[i+1]:
                b_index = i+1
                break

        old_b_index = b_index
        for times in range(3):
            if a_index == old_b_index:
                output_str += 'B'
                b_index += 1
            elif b_index == len(num_list):
                output_str += 'A'
                a_index += 1
            else:
                if num_list[a_index] < num_list[b_index]:
                    output_str += 'A'
                    a_index += 1
                else:
                    output_str += 'B'
                    b_index += 1

        print(output_str)