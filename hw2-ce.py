import math

def factor_sum(n):
    s = 1
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            s += i
            s += int(n/i)
    return s

def is_perfect(n):
    s = 1
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            s += i
            s += int(n/i)
    if s == n:
        return True
    else:
        return False

if __name__ == '__main__':
    n = 28
    print(factor_sum(n))
    print(is_perfect(n))