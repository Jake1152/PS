def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a_idx = 0
    b_idx = 0
    while len(B) > b_idx:
        if A[a_idx] < B[b_idx]:
            a_idx += 1
            answer += 1
        b_idx += 1
    
    return answer

'''
A팀의 숫자가 공개된 상태에서
B팀이 이길수 있는 최대 경우의 수 return
'''
