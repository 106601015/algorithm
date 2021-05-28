if __name__ == '__main__':
    c = int(input())
    for i in range(c):
        a, b = input().split(' ')
        a, b = int(a), int(b)
        if a % 2 == 1:
            a += 1
        if b % 2 == 0:
            b += 1

        total_sum = 0
        for j in range(a, b, 2):
            total_sum += j

        print('Case {}: {}'.format(str(i+1), str(total_sum)))