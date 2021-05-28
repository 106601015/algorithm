import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        a, b = input().split(' ')
        a, b = int(a), int(b)
        answer = 0
        for j in range(a, b+1):
            if j % 2 == 1 and not is_prime(j):
                answer += j
        print(answer)
