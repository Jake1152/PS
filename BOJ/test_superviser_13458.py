from sys import stdin

input = stdin.readline
exam_venue_cnt = int(input())
taker_cnt_list = list(map(int, input().split()))
main_supervisor_cover_cnt, sub_supervisor_cover_cnt = map(int, input().split())
supervisor_cnt = 0
for taker_cnt in taker_cnt_list:
    if (taker_cnt < main_supervisor_cover_cnt):
        supervisor_cnt += 1
        continue
    mod = taker_cnt - main_supervisor_cover_cnt
    if (mod % sub_supervisor_cover_cnt == 0):
        sub_supervisor_cnt = mod // sub_supervisor_cover_cnt
    else: 17  15  16
        sub_supervisor_cnt = mod // sub_supervisor_cover_cnt + 1    
    supervisor_cnt += 1 + sub_supervisor_cnt
print(supervisor_cnt)