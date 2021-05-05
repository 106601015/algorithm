'''
def QuickSort_lastPivot(num_list, lb, rb):
    print(num_list)
    if lb >= rb:
        return num_list
    p = num_list[rb]
    l = lb
    r = rb - 1

    while True:
        while num_list[l] < p:
            l += 1
        while num_list[r] >= p:
            r -= 1
            if r == lb:
                break
        if l < r:
            buffer = num_list[l]
            num_list[l] = num_list[r]
            num_list[r] = buffer
        else:
            break

    buffer = num_list[rb]
    num_list[rb] = num_list[l]
    num_list[l] = buffer

    QuickSort_lastPivot(num_list, lb, l-1)
    QuickSort_lastPivot(num_list, l+1, rb)
    return num_list
'''
def QuickSort_firstPivot(num_list, lb, rb):
    # if null list
    if lb >= rb:
        return num_list
    # set pivot, left index and right index
    p = num_list[lb]
    l = lb + 1
    r = rb

    while True:
        # set l->big, r->small
        while num_list[l] < p:
            l += 1
        while num_list[r] >= p:
            r -= 1
            # if r to boundary
            if r == lb:
                break

        # l r exchange and show
        if l < r:
            buffer = num_list[l]
            num_list[l] = num_list[r]
            num_list[r] = buffer
            #print(l, r, num_list[l], num_list[r])
            print_list(num_list)
        # if l meet r
        else:
            break

    # lb r exchange and show
    buffer = num_list[lb]
    num_list[lb] = num_list[r]
    num_list[r] = buffer
    #print(lb, r, num_list[lb], num_list[r])
    #print_list(num_list)

    # divide to two parts
    QuickSort_firstPivot(num_list, lb, l-1)
    QuickSort_firstPivot(num_list, l+1, rb)
    return num_list

def print_list(num_list):
    output_str = ''
    for n in num_list:
        output_str += str(n)+' '
    print(output_str[:-1])

if __name__ == '__main__':
    num_of_input = int(input())
    num_list = list(map(int, input().split(' ')))
    buffer = 0

    print_list(num_list) #begin
    QuickSort_firstPivot(num_list, 0, num_of_input-1)