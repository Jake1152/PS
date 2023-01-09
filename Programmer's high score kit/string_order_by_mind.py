def solution(strings, n):
    answer = []
    answer.append(strings[n])
    # rted_arr = sorted(dicList, key=lambda e: (-e['point'], e['penalty']))
    return sorted(strings, key = lambda x: (x[n], x), reverse=False)