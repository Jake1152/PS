def solution(d, budget):
    begin = 0
    end = len(d) - 1
    d.sort()
    while (begin == end):
        mid = (begin + end) // 2
        if budget == sum(d[:mid+1]):
            return end
        elif (begin < end):
            end = mid - 1
        else:
            begin = mid + 1
    return begin
'''
주어진 예산에 딱 맞으면서
최대한 많은 물품을 살때의
물품의 갯수 리턴

파라메트릭 서치인줄 알았으나
백트레킹하며 완전탐색을 하여야 가능할것이라 생각든다.
'''