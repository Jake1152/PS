# 중량제한 1936
from collections import defaultdict, deque

def bfs(start, target):
	queue = deque()
	queue.append(start)
	while (queue):
		cur_node = queue.pop()
		#방문 안했던 경우
		if visited[cur_node] == False:
			visited[cur_node] = True
			# target을 찾은 경우
			if cur_node == target:
				result_weight.append()
				pass
			for key in cur_node.key():
				queue.append(key)

N, M = map(int, input().split())
node = {i: defaultdict(int) for i in range(1, N + 1)}
visited = [False for _ in range(N)]
result_weight = []
# 노드에 연결된 정점을 이중 dict로 연결, 인접한 노드간에 연결이 2개 이상이면 weight가 큰 것만 연결한다.
# dict[from_node][to_node] -> weight
for _ in range(M):
	a_node, b_node, weight = map(int, input().split())
	# 인접한 노드간에 연결이 2개 이상이면 weight가 큰 것만 연결한다.
	if (node[a_node][b_node] < weight):
		node[a_node][b_node] = weight
		node[b_node][a_node] = weight

start_node, target_node = map(int, input().split())

print(f"{node=}")


'''
visited
어떻게 처리?


'''