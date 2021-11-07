# 6068 시간 관리하기
from sys import stdin
input = stdin.readline

tasks = []
n = int(input())
for _ in range(n):
    tasks.append(tuple(map(int, input().split())))

# 마감시한을 기준으로 내림차순으로 정렬
tasks_sorted = sorted(tasks, key = lambda x: x[1], reverse=True)
# 가장 늦은 마감시한
cur_time = tasks_sorted[0][1]
for working_time, dead_line in tasks_sorted:
    # 계산된 현재 시간이 마감시한보다 이후에 있으면 햔재 작업의 마감시한으로 앞 당김
    if cur_time > dead_line:
        cur_time = dead_line
    cur_time -= working_time
    
if cur_time < 0:
    print(-1)
else:
    print(cur_time)
