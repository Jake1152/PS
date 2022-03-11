import heapq
import sys

def dijkstra(start):
	# 초기배열 설정
	distances = {node: sys.maxsize for node in graph}
	# 시작 노드의 거리는 0으로 설정
	distances[start] = 0
	queue = []
	'''
	시작 노드부터 탐색하기 위함
	(거리, 노드)
	거리, 노드 순으로 넣은 이유는 heapq 모듈에 첫번쨰 데이터를 기준으로 정렬ㄹ을 진행하기 때문
	(노드, 거리) 순으로 넣으면 최소힘 예상한대로 정렬하지 않는다고 함
	'''
	heapq.heappush(queue, (distances[start], start))
	
	# 우선순위 큐에 데이터가 하나도 없을 때까지 반복
	while queue:
		# 가장 낮은 거리를 가진 노드와 거리를 추출
		current_distance, node = heapq.heappop(queue)
		if distances[node] < current_distance:
			continue
		
		# 대상인 노드에서 인접한 노드와 거리를 순회
		for adjacency_node, distance in graph[node].items():
			# 현재 노드에서 인접한 노드를 지나갈 때까지의 거리를 더한다.
			weighted_distance = current_distance + distance
			# 배열의 저장딘 거리보다 위의 가중치가 더 작으면 해당 노드의 거리 변경
			if weighted_distance < distances[adjacency_node]:
				# 배열에 저장된 거리보다 가중치가 더 작으므로 변경
				distances[adjacency_node] = weighted_distance
				# 다음 인접 거리를 계산하기 위해 우선 순위 큐에 삽입 (노드가 동일해도 일단 다 저장함)
				heapq.heappush(queue, (weighted_distance, adjacency_node))
	return distances
		
graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'C': 1, 'D': 2},
    'C': {'B': 4, 'D': 8, 'E': 2},
    'D': {'E': 7},
    'E': {'D': 9},
}

result = dijkstra('A')
print(result)

# {'A': 0, 'B': 7, 'C': 3, 'D': 9, 'E': 5}