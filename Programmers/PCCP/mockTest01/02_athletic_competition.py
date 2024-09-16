'''
문제해결방법

그리디?
부분의 최적이 전체의 최적이 될지 알 수 없음

완전탐색으로 처리
10! => 약 360만
'''
from itertools import permutations

# 5명 중 3명
def yield_permutation(ability):
    for permute in permutations(ability, len(ability[0])):
        yield permute

def solution(ability):
    answer = 0
    for permutations_list in yield_permutation(ability):
    # for permutations_list in permutations(ability, len(ability[0])):
        idx = 0
        temp = 0
        for permute in permutations_list:
            temp += permute[idx]
            idx += 1
        answer = max(temp, answer)
        # answer = max(answer, sum(permute))
    return answer
