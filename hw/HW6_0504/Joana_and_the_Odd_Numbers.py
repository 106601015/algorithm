def linelength_to_lastnum(linelength):
    return int(2*((linelength+1)/2)**2-1)

if __name__ == '__main__':
    num_of_input = int(input())
    for buffer in range(num_of_input):
        linelength = int(input())
        lastnum = linelength_to_lastnum(linelength)
        print(lastnum * (lastnum-2) * (lastnum-4))