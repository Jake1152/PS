def solution(d, budget):
	answer = 0    
	d.sort()
	while budget > 0:
		if budget - d[0] >= 0:
			budget -= d.pop(0)
			answer += 1
		else:
			return answer
	return answer

'''
주어진 예산에 딱 맞으면서
최대한 많은 물품을 살때의
물품의 갯수 리턴

파라메트릭 서치인줄 알았으나
백트레킹하며 완전탐색을 하여야 가능할것이라 생각든다.
stack으로 푸는 방법
'''