import math

def is_relatively_prime(i, num):
    # toss and divide
    while True:
        if i > num:
            i -= num
        else:
            num -= i

        if i == 0 or num == 0:
            break

    if i + num != 1:
        return False
    else:
        return True

if __name__ == '__main__':
    num_of_input = int(input())
    for buffer in range(num_of_input):
        num = int(input())
        counter = 0

        if num == 1:
            print(1)
        else:
            for i in range(1, num):
                if is_relatively_prime(i, num):
                    counter += 1
            print(counter)