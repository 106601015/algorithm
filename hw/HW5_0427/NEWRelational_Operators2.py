if __name__ == '__main__':
    while True:
        input_str = input()
        if input_str[0] == '0':
            break
        a, b = input_str.split(' ')
        a, b = int(a), int(b)

        if a > b:
            print('>')
        elif a < b:
            print('<')
        else:
            print('=')