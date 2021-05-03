def improved_bubble_sort(A):
    for i in range(len(A)-1, 0, -1):
        flag = False
        for j in range(i):
            if A[j] > A[j+1]:
                buffer = A[j]
                A[j] = A[j+1]
                A[j+1] = buffer
                flag = True
        if not flag:
            break

if __name__ == '__main__':
    #20 30 40 100 70 60 50 40
    #A = list(map(int, input().split(' ')))
    #improved_bubble_sort(A)
    print(locals(), type(locals()))