# dfs, bfs 1260

import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

def dfs(node):
	print(node, end=' ')
	visited[node] = True
	for adj_node in edges[node]:
		if visited[adj_node] == False:
			dfs(adj_node)

def bfs(node):
	queue = deque([node])
	while queue:
		# print(f"{queue=}")
		cur_node = queue.popleft()
		if visited[cur_node] == False:
			# print(f"{cur_node=}")
			print(cur_node, end=' ')
			visited[cur_node] = True
			queue += edges[cur_node]

n, m, v = map(int, input().split())
edges = defaultdict(list)
for _ in range(m):
	from_node , to_node = map(int, input().split())
	edges[from_node].append(to_node)
	edges[to_node].append(from_node)

for node in range(1, n+1):
	edges[node].sort()

for i in range(1,2+1):
	if i == 1:
		visited = [ False for _ in range(n+1) ]
		dfs(v)
	else:
		visited = [ False for _ in range(n+1) ]
		bfs(v)
	print()
