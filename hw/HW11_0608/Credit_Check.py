if __name__ == '__main__':
    num_of_cases = int(input())
    for case_i in range(num_of_cases):
        input_str = input()
        total = 0
        is_even_flag = True

        for ch in input_str:
            if ch == ' ':
                pass
            elif is_even_flag:
                double = 2*int(ch)
                if double >= 10:
                    total += (double%10 + 1)
                else:
                    total += double
                is_even_flag = not is_even_flag
            else:
                total += int(ch)
                is_even_flag = not is_even_flag

        if total%10 == 0:
            print('Valid')
        else:
            print('Invalid')