def find_perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        return True
    else:
        return False

def find_happy(n):
    item_limit = 100
    counter = 0
    while n != 1:
        s = 0
        while n >= 1:
            s += (n%10)**2
            n //= 10
        n = s
        counter += 1
        #print(counter, n)
        if counter > item_limit:
            return False
    return True

if __name__ == '__main__':
    print('perfect?? :', find_perfect(n = 28))
    print('happy?? :', find_happy(n = 58))