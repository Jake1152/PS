from collections import deque

def solution(n, t, m, timetable):
    min_timetable = deque()
    for time in timetable:
        min_timetable.append(int(time[:2]) * 60 + int(time[3:]))
        
    cur_time = 9 * 60
    midnight = 24 * 60
    leaving_time = cur_time + t if n > 1 else midnight - 1
    just_in_time_candidate = []
    while (cur_time < midnight):
        #leaving_time
        if (leaving_time == cur_time):
            cnt = [m][0]
            shuttle = []
            while (cnt and min_timetable):
                # print(f"{min_timetable=}")
                crew = min_timetable[0]
                if crew <= leaving_time:
                    shuttle.append(min_timetable.popleft())
                cnt -= 1
            # 셔틀에 다 탄 경우와 못 탄 경우로 나눔
            if len(shuttle) < m:
                just_in_time_candidate.append(shuttle[-1])
            else: # 1분만 더 일찍온다
                just_in_time_candidate.append(shuttle[-1] - 1)
            leaving_time += t
        cur_time += 1
    answer = ""
    hour = just_in_time_candidate[-1] // 60
    if hour < 10:
        answer += "0" + str(hour)
    else:
        answer += str(hour)
    answer += ":"
    minute = just_in_time_candidate[-1] % 60
    if minute < 10:
        answer += "0" + str(minute)
    else:
        answer += str(minute)    
    return answer 


n = 1
t = 1
m = 5
timetable =	["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable))

# 파이썬 헤더파일