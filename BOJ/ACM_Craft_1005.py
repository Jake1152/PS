from collections import defaultdict
from sys import stdin

input = stdin.readline
test_case = int(input())
def calculate_entry_degree(adj_list, entry_degree):
	for from_node in adj_list.keys():
		for to_node in adj_list[from_node]:
			entry_degree[to_node] += 1

#테스트 케이스별 처리
for _ in range(test_case):
	adj_list = defaultdict(list)
	buildings, construction_rules = map(int, input().split())
	entry_degree = [0 for _ in range(buildings+1)]
	# index 0은 쓰지않고 1번부터 시작되게 하기 위함
	construction_durations = [0]
	construction_durations += list(map(int, input().split()))
	# 설치시간을 반영
	resul_construction_durations = [ element for element in construction_durations]
	# 어떤 순서로 건설되는지 룰 저장 ㄴㄱ
	for _ in range(construction_rules):
		from_build, to_build = map(int, input().split())
		adj_list[from_build].append(to_build)
	find_node = int(input())
	# 진입차수를 노드별로 계산
	calculate_entry_degree(adj_list, entry_degree)
	# 중복제거!!
	visited = [ True for _ in range(buildings+1)]
	while (True):
		entry_degree_sum = 0
		for node in range(1, buildings+1):
			entry_degree_sum += entry_degree[node]
			if visited[node] and entry_degree[node] == 0:
				for adj_node in adj_list[node]:
					# 인근의 진입차수가 더 높은 노드가 현재까지 계산되어 있지 않다면 인접 노드의 건설비용에 나의 노드의 건설비용을 더한다.
					if resul_construction_durations[adj_node] == construction_durations[adj_node]:
						resul_construction_durations[adj_node] += resul_construction_durations[node]
					else:
						resul_construction_durations[adj_node] = \
								max(resul_construction_durations[adj_node], \
									construction_durations[adj_node] + resul_construction_durations[node])
					entry_degree[adj_node] -= 1
				visited[node] = False
		if entry_degree_sum == 0:
			break
	print(resul_construction_durations[find_node])



'''
1
2 1
1 1
2 1
1
정답: 2
출력: 1

2
4 4
10 100 1 10
2 4
3 4
1 2
1 3
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7
'''

