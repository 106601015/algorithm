def fine_fibonacci(n):
    fibonacci = [1, 1]
    if n < 1:
        return 0
    elif n == 1 or n == 2:
        return 1

    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
    return fibonacci[n-1]

if __name__ == '__main__':
    num_of_input = int(input())
    for i in range(num_of_input):
        print(str(fine_fibonacci(int(input()))))
