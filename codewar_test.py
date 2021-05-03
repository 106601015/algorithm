# input : 正整n
# output : 一個正整數series, 不重複項數，每一項平方和總和==n**2

# ex:
# decompose 50 returns "1,3,5,8,49"
# decompose 4  returns "Nothing"

# 終止條件：尾端小數總和<n**2 or series_boolean == True
import math

def decompose(n):
    series = []
    recu_loop(n**2, series)

def recu_loop(square_sum, series):
    print('square_sum:', square_sum)
    #upper_bound = int(math.sqrt(square_sum))
    upper_bound = math.ceil(math.sqrt(square_sum)) -1
    lower_bound = get_lower_bound(square_sum) -1
    print('ul:' ,upper_bound, lower_bound)
    for i in range(upper_bound, lower_bound, -1):
        inner_square_sum = square_sum - i**2
        series.append(i)
        if inner_square_sum == 0:
            print('finded!! :', series)
            break
        recu_loop(inner_square_sum, series)

def get_lower_bound(input_sum):
    s, n = 0, 1
    while s < input_sum:
        s += n**2
        n += 1
    return n-1

if __name__ == "__main__":
    decompose(11)