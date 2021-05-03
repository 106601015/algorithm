if __name__ == '__main__':
    c = int(input())
    for i in range(c):
        n_score_str = input()
        n = int(n_score_str.split(' ')[0])
        score_sum = 0
        for score in n_score_str.split(' ')[1:]:
            score_sum += int(score)
        average = score_sum/n

        higher_count = 0
        for score in n_score_str.split(' ')[1:]:
            if int(score) > average:
                higher_count += 1
        print('{:.3f}%'.format(higher_count*100/n))
        #return '{:.3f}%'.format(higher_count*100/n)
