def cover_line(cost):
    n, e = len(cost), len(cost[0])
    cost_copy = []
    for i in range(n):
        cost_copy.append(cost[i][:])
    lines_num = 0
    cover_row_lines, cover_col_lines = [], []
    while True:
        zero_covered_list = []
        # row
        for i in range(n):
            counter = 0
            for j in range(e):
                if cost_copy[i][j] == 0:
                    counter += 1
            zero_covered_list.append(counter)
        # col
        for j in range(e):
            counter = 0
            for i in range(n):
                if cost_copy[i][j] == 0:
                    counter += 1
            zero_covered_list.append(counter)
        # cover
        max_index = zero_covered_list.index(max(zero_covered_list))
        if max_index < n:
            for j in range(e):
                cost_copy[max_index][j] += 1
            cover_row_lines.append(max_index)
        else:
            for i in range(n):
                cost_copy[i][max_index-n] += 1
            cover_col_lines.append(max_index-n)

        # check if 0 exists
        zero_num_recoder = 0
        for i in range(n):
            for j in range(e):
                if cost_copy[i][j] == 0:
                    zero_num_recoder += 1
        lines_num += 1
        if zero_num_recoder == 0:
            break
    return cover_row_lines, cover_col_lines, lines_num
def cover_done(cost, score):
    #print('in cover_done!!!')
    n, e = len(cost), len(cost[0])
    target_location = []
    selected_row, selected_col = [], []
    while len(target_location) != n:
        # row check zero
        for i in range(n):
            zero_num_recoder = 0
            for j in range(e):
                if cost[i][j] == 0:
                    only_j = j
                    zero_num_recoder += 1
            if zero_num_recoder == 1 and (i, only_j) not in target_location and i not in selected_row and j not in selected_col:
                target_location.append((i, only_j))
                selected_row.append(i)
                selected_col.append(only_j)
        #print(target_location, selected_row, selected_col)

        # col check zero
        for j in range(e):
            zero_num_recoder = 0
            for i in range(n):
                if cost[i][j] == 0:
                    only_i = i
                    zero_num_recoder += 1
            if zero_num_recoder == 1 and (only_i, j) not in target_location and i not in selected_row and j not in selected_col:
                target_location.append((only_i, j))
                selected_row.append(only_i)
                selected_col.append(j)
        #print(target_location, selected_row, selected_col)

        # other
        for i in range(n):
            for j in range(e):
                if cost[i][j] == 0 and i not in selected_row and j not in selected_col:
                    target_location.append((i, j))
                    selected_row.append(i)
                    selected_col.append(j)
        #print(target_location, selected_row, selected_col)
        #exit()

    # calculate total score
    total_score = 0
    for location in target_location:
        total_score += score[location[0]][location[1]]
    print(total_score)
    exit()

if __name__ == '__main__':
    input_int_list = list(map(int, input().split(' ')))
    n, e = input_int_list[0], input_int_list[1]
    score = []
    for i in range(n):
        score.append(list(map(int, input().split(' '))))

    # max score -> min cost
    max_score = 0
    for i in range(n):
        for j in range(e):
            if score[i][j] > max_score:
                max_score = score[i][j]
    cost = []
    for i in range(n):
        cost.append([])
        for j in range(e):
            cost[i].append(max_score-score[i][j])

    # step1, row substraction
    for i in range(n):
        min_cost = 999
        for j in range(e):
            if cost[i][j] < min_cost:
                min_cost = cost[i][j]
        for j in range(e):
            cost[i][j] -= min_cost

    # step2, cover zero by line
    cover_row_lines, cover_col_lines, lines_num = cover_line(cost)
    if lines_num == n:
        cover_done(cost, score)

    # step3, col substraction
    for j in range(e):
        min_cost = 999
        for i in range(n):
            if cost[i][j] < min_cost:
                min_cost = cost[i][j]
        for i in range(n):
            cost[i][j] -= min_cost

    # step4, cover zero by line
    cover_row_lines, cover_col_lines, lines_num = cover_line(cost)
    if lines_num == n:
        cover_done(cost, score)

    # step5, extend
    while True:
        # find no cover min element
        min_cost = 999
        for i in range(n):
            for j in range(e):
                if cost[i][j] < min_cost and i not in cover_row_lines and j not in cover_col_lines:
                    min_cost = cost[i][j]
        # extend
        for i in range(n):
            for j in range(e):
                cost[i][j] -= min_cost
                if i in cover_row_lines:
                    cost[i][j] += min_cost
                if j in cover_col_lines:
                    cost[i][j] += min_cost
        # step4, cover zero by line
        cover_row_lines, cover_col_lines, lines_num = cover_line(cost)
        if lines_num == n:
            cover_done(cost, score)
'''
4 4
120 155 159 113
175 133 184 152
134 141 132 104
176 174 182 168
'''