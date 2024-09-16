'''
heap 사용
우선순위와 호출된 시각 기준
[우선순위, 호출된 시각, 실행시간]
'''

from queue import PriorityQueue
def solution(programs):
    que = PriorityQueue()
    for program in programs:
        priority, call_time, runtime = program
        print(f"{priority=}, {call_time=}, {runtime=}")
        que.put((priority, call_time))
    while (not que.empty()):
        print(f"{que.get()=}")
        
    answer = []
    return answer
