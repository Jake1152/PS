#relatino_cal_2644
from collections import defaultdict
from collections import deque
people_cnt = int(input())
init_node, target_node = map(int, input().split())
relation_cnt = int(input())
visited = [True for _ in range(people_cnt+1)]
dis = [0 for _ in range(people_cnt+1)]
graph = defaultdict(list)

for _ in range(relation_cnt):
	start_node, end_node = map(int, input().split())
	graph[start_node].append(end_node)
	graph[end_node].append(start_node)

queue = deque([init_node])
while (queue):
	cur_node = queue.popleft()
	visited[cur_node] = False
	for adj_node in graph[cur_node]:
		if visited[adj_node]:
			queue.append(adj_node)
			dis[adj_node] = dis[cur_node] + 1
			if adj_node == target_node:
				break
# print(f"{dis=}")
if init_node != target_node and dis[target_node] == 0:
	print(-1)
else:
	print(dis[target_node])
