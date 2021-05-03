def DC_rank(s):
    print('DC_rank begin, len(s)={}'.format(str(len(s))), s)
    rank_recoder = {}

    # step1, if n=1 then that point rank = 0, return rank_recoder
    if len(s) == 1:
        rank_recoder[s[0][0]] = 0
        return rank_recoder
    # step2, split s to sl & sr
    s_x_sorted = sorted(s, key=lambda ss: ss[0])
    sl, sr = s_x_sorted[:int(len(s_x_sorted)/2)], s_x_sorted[int(len(s_x_sorted)/2):]
    # step3, recursive using DC_rank and merge rank_recoder
    rank_recoder_sl, rank_recoder_sr = DC_rank(sl), DC_rank(sr)
    rank_recoder.update(rank_recoder_sl)
    rank_recoder.update(rank_recoder_sr)
    # step4, s sorted by Y and scand, if sl->count+=1, if sr->point rank+=count, return rank_recoder
    print('step4 rank_recoder:', rank_recoder)
    s_y_sorted = sorted(s, key=lambda ss: ss[1])
    count = 0
    for point in s_y_sorted:
        if point in sl:
            count += 1
        elif point in sr:
            rank_recoder[point[0]] += count
        else:
            print('wtf')
    return rank_recoder

if __name__ == '__main__':
    s = [(1, 4), (2, 2), (3, 5), (4, 8), (5, 6), (6, 3), (7, 9), (8, 7)]
    print('rank_recoder: ', DC_rank(s))