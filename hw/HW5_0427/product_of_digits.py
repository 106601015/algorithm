import math

def find_feasible_factor(num):
    feasible_list = []
    i = 2
    while num >= 10:
        if num % i == 0:
            num /= i
            feasible_list.append(i)
            i = 2
        else:
            i += 1

        if i == 7:
            return []
    feasible_list.append(int(num))
    return feasible_list

if __name__ == '__main__':
    num_of_input = int(input())
    for buffer in range(num_of_input):
        num = int(input())
        if num < 10:
            print(num)
        else:
            feasible_list = find_feasible_factor(num)
            #print('feasible_list:', feasible_list)
            if feasible_list == []:
                print(-1)
            else:
                output_str = ''
                for i in feasible_list:
                    output_str += str(i)
                print(output_str)