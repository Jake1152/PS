import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

# 방향성 없는 그래프이므로 x,y일 떄와 y, x일 때 모두 추가
for _ in range(e):
	x, y, cost = map(int, input().split())
	q = []
	graph[x].append((y, cost))
	graph[y].append((x, cost))

def dijkstra(start):
	distance = [INF] * (v + 1)
	heapq.heappush(q, (0, start))
	distance[start] = 0
	
	while q:
		dist, now = heapq.heappop(q)
		
		if distance[now] < dist:
			continue
		
		for i in graph[now]:
			cost = dist + i[1]
		
			if distance[i[0]] > cost:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))
	
	#반환값은 최단 거리 배열
	return distance
	
v1, v2 = map(int, input().split())

# 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[v]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[v]

result = min(v1_path, v2_path)
print(result if result < INF else -1)



'''
#special shortest path 1504
import sys
import heapq
from collections import defaultdict

def dijkstra(start):
	# 초기배열 설정
	distances = {node: sys.maxsize for node in graph}
	# 시작 노드의 거리는 0으로 설정
	distances[start] = 0
	queue = []
	
	# 시작 노드부터 탐색하기 위함
	# (거리, 노드)
	# 거리, 노드 순으로 넣은 이유는 heapq 모듈에 첫번쨰 데이터를 기준으로 정렬ㄹ을 진행하기 때문
	# (노드, 거리) 순으로 넣으면 최소힘 예상한대로 정렬하지 않는다고 함
	
	heapq.heappush(queue, (distances[start], start))
	
	# 우선순위 큐에 데이터가 하나도 없을 때까지 반복
	while queue:
		# 가장 낮은 거리를 가진 노드와 거리를 추출
		current_distance, node = heapq.heappop(queue)
		if distances[node] < current_distance:
			continue
		
		# 대상인 노드에서 인접한 노드와 거리를 순회
		for adjacency_node, distance in graph[node]:
			print(f"{adjacency_node=}")
			print(f"{distance=}")
			# 현재 노드에서 인접한 노드를 지나갈 때까지의 거리를 더한다.
			weighted_distance = current_distance + distance
			# 배열의 저장딘 거리보다 위의 가중치가 더 작으면 해당 노드의 거리 변경
			if weighted_distance < distances[adjacency_node]:
				# 배열에 저장된 거리보다 가중치가 더 작으므로 변경
				distances[adjacency_node] = weighted_distance
				# 다음 인접 거리를 계산하기 위해 우선 순위 큐에 삽입 (노드가 동일해도 일단 다 저장함)
				heapq.heappush(queue, (weighted_distance, adjacency_node))
	return distances
		

input = sys.stdin.readline
graph = defaultdict(list)
# 그래프 인접 리스트 구성
N, E = map(int, input().split())
for _ in range(E):
	u, v, w = map(int ,input().split())
	graph[u].append((v, w))
v1, v2 = map(int, input().split())
print(f"{graph=}")

result = dijkstra(2)
print(result)



'''