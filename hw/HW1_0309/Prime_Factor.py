if __name__ == '__main__':
    origin_n = int(input())
    n = origin_n
    recorder, content = [], [] # factor counter recorder 2~n
    factor, counter = 2, 0

    while True:
        if n % factor == 0:
            n /= factor
            counter += 1
        else:
            if counter != 0:
                content = [factor, counter]
                recorder.append(content)
            factor += 1
            counter = 0
            if factor > n: #n == 1 no need
                break

    s = '{}='.format(str(origin_n))
    for content in recorder:
        factor, counter = content[0], content[1]
        if counter == 1:
            s += str(factor)+'*'
        else:
            s += str(factor)+'^'+str(counter)+'*'
    print(s[:-1])
