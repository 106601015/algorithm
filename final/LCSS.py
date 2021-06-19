def LCSS(x, y):
    m, n = len(x), len(y)
    c, b = [], []
    for i in range(m+1):
        c.append([])
        b.append([])
        for j in range(n+1):
            c[i].append(-1)
            b[i].append(-1)

    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = 'b' # b==both
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 'u' # u==up
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 'l' # l==left
    #print(c)
    #print(b)

    return c[-1][-1]

if __name__ == "__main__":
    cases_num = int(input())
    for case_i in range(cases_num):
        x = input()
        y = input()
        print(LCSS(x, y))