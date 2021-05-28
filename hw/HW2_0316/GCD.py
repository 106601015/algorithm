if __name__ == '__main__':
    c = int(input())
    for i in range(c):
        a, b = input().split(' ')
        a, b = int(a), int(b)

        while True:
            if a > b:
                a -= int(a/b) * b
            else:
                b -= int(b/a) * a

            if a == 0 or b == 0:
                print(a+b)
                break