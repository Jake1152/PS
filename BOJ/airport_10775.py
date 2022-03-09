from sys import stdin
from collections import defaultdict
input = stdin.readline
gate = int(input())
plane = int(input())
docker_dict = defaultdict(int)
result = 0

for _ in range(plane):
	plane = int(input())
	# 이전에 들어온 가능 큰 숫자의 비행기 번호도 있어야한다.
	posi_min = gate
	posi_max = 1
	for plane_num in range(plane,0,-1):
		# print(f"{plane_num=}")
		if gate >= plane_num and docker_dict[plane_num] == 0:
			docker_dict[plane_num] = 1
			if plane_num < posi_min:
				posi_min = plane_num
			if plane_num > posi_max:
				posi_max = plane_num
			result += 1
			
			break
	else:
		break
	
print(result)

'''
일반적인 이분탐색과 다른 케이스
어떻게하면 빠르게 적절한 게이트를 찾을 수 있는지 고민이 필요하다
조건은 
현재 도킹할 수 있는 가장 숫자가 큰 게이트를 찾아서 도킹한다.
만약 10만번이라는 비행기가 10만번 들어오는경우
첫번째 들어오는 10만번 비행기는 10만 게이트에 한 번에 도킹가능하지만
마지막에 들어온느 비행기는 10만번의 검색시간이 소요된다.
기존 이분탐색으로 안되는 부분은 
고를 수 있는 수 중에 가장 커야한다.
가능한 게이트가 아래와 같고 10번 비행기가 들어왔을떄
최적은 7이다.
하지만 이것을 어떻게 찾을 것인가?
1 2 3 4 5 6 7 8 9 10
o o o o o x o x x x
'''
