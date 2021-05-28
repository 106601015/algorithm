def insertion_sort(num_list):
    swaps_counter = 0
    for picked_index in range(1, len(num_list)):
        loop_swaps_counter = 0
        for compare_index in range(picked_index-1, -1, -1):
            # if sort ok
            if num_list[picked_index] < num_list[compare_index]:
                loop_swaps_counter += 1
            else:
                picked_value = num_list.pop(picked_index)
                num_list.insert(picked_index - loop_swaps_counter, picked_value)
                swaps_counter += loop_swaps_counter
                break

            # if minest
            if compare_index == 0:
                picked_value = num_list.pop(picked_index)
                num_list.insert(picked_index - loop_swaps_counter, picked_value)
                swaps_counter += loop_swaps_counter
                break

    return num_list, swaps_counter

if __name__ == '__main__':
    while True:
        num_of_input = int(input())
        num_list = []

        if num_of_input == 0:
            break
        for str_num in input().split(' '):
            num_list.append(int(str_num))

        num_list, swaps_counter = insertion_sort(num_list)
        print('Optimal swapping takes {} swaps.'.format(swaps_counter))