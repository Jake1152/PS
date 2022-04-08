from collections import defaultdict
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
	# 진입차수를 노드별로 계산
	calculate_entry_degree(adj_list, entry_degree)
	for node in range(1, buildings+1):
		if node == 0:
			for adj_node in adj_list[node]:
				entry_degree[adj_node] -= 1





