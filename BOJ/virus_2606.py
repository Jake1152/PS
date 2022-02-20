# virus 2606
from collections import deque
from collections import defaultdict

computers = int(input())
network_cnt = int(input())
graph = defaultdict(list)
visited = [True] * (computers+1)
for _ in range(network_cnt):
	a_node, b_node = map(int, input().split())
	graph[a_node].append(b_node)
	graph[b_node].append(a_node)

# for com_num in range(1, len(computers)+1):
# 1번 컴퓨터는 기본 숙주라서 카운팅하지 않는다.
infected_cnt = -1
queue = deque([1])
while queue:
	pop_node = queue.popleft()
	if visited[pop_node]:
		print(f"{pop_node=}")
		visited[pop_node] = False
		queue += graph[pop_node]
		infected_cnt += 1
print(infected_cnt)
