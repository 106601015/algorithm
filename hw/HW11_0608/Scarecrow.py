if __name__ == '__main__':
    num_of_cases = int(input())
    for case_i in range(num_of_cases):
        num_of_str = int(input())
        input_str = input()
        assert len(input_str)==num_of_str

        num_of_scarecrow = 0
        scarecrow_effective_range = 3
        new_scarecrow_occupation = 0
        i = 0
        while i<num_of_str:
            if input_str[i] == '#':
                pass
            elif input_str[i] == '.':
                i += 2
                num_of_scarecrow += 1
            else:
                print('!!! simble error !!!')
            i += 1

        print('Case {}: {}'.format(str(case_i+1), str(num_of_scarecrow)))