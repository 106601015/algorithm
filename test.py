import os
import numpy as np

def p(i):
    print(i)
    if i == 5:
        exit()

if __name__ == '__main__':
    '''
    a = np.array([[[1, 2], [3, 4], [5, 6]], [[11, 12], [13, 14], [15, 16]], [[21, 22], [23, 24], [25, 26]], [[31, 32], [33, 34], [35, 36]]])
    print(a.shape)
    print(a)
    a = np.reshape(a, (3, 2, 4))
    print(a.shape)
    print(a)
    '''
    '''
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = a
    c = a[:]
    d = []
    d.extend(a)
    e = [[], [], []]
    for i in range(3):
        for j in range(3):
            e[i].append(a[i][j])

    print(a, b, c, d, e)

    a[0].pop()
    a[1].append(5)

    print(a, b, c, d, e)
    '''

    a = [1, 2, 3, 5, 5]
    b = a.index(max(a))
    print(b)

    '''
    for i in range(10):
        p(i)
    '''