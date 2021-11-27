line_cnt = int(input())
for _ in range(line_cnt):
    cur_list = list(map(int,input().split()))
    mean_score = sum(cur_list[1:]) // cur_list[0]
    over_mean = 0
    for score in cur_list[1:]:
        if score > mean_score:
            over_mean += 1
    print("{:.3f}%".format(over_mean/cur_list[0]  * 100))