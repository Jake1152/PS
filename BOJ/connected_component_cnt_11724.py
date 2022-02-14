# connected element count 11724
import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
input = sys.stdin.readline

#2. way, dfs
'''
1. 인접노드들을 다 연결한다.
2. 모든 정점을 방문할때까지 dfs를 한다.
'''
def dfs(node):
	visited[node] = True
	# print(f"{node=} in dfs")
	for adj_node in edges[node]:
		# print(f"{adj_node=}")
		if visited[adj_node] == False:
			dfs(adj_node)

n, m = map(int, input().split())
edges = defaultdict(list)
for _ in range(m):
	u, v = map(int, input().split())
	edges[u].append(v)
	edges[v].append(u)

visited = [ False for _ in range(n+1)]
# visited[0] = True
cnt = 0
for node in range(1, n+1):
	if visited[node] == False:
		dfs(node)
		cnt += 1
print(cnt)



'''
#1. way, union-find
def find_parent(x):
	if parent[x] != x:
		parent[x] = find_parent(parent[x])
	# print(f"{x=}, {parent[x]=}")
	return parent[x]

def union_parent(a, b):
	# print("=== union parent")
	a = find_parent(a)
	b = find_parent(b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
# print(f"{parent=}")
edges = []
result = 0

for _ in range(m):
	from_node, to_node= map(int, input().split())
	edges.append([from_node, to_node])

for a_node, b_node in edges:
	a_parent = find_parent(a_node)
	# print(f"{a_parent=}")
	b_parent = find_parent(b_node)
	# print(f"{b_parent=}")
	if a_parent != b_parent:
		union_parent(a_node, b_node)
	# print(f"{parent=}")

for node_idx in range(1, n + 1):
	parent[node_idx] = find_parent(node_idx)
# print(f"after loop {parent=}")

parent = list(set(parent))
# indexing의 문제로 0번부터 시작해서 1개를 빼서 return 시킨다.
print(len(parent)-1)
# print(f"{parent=}")

'''



'''
union-find
- init
	처음에 정점별 선언
- find
	root만 찾으면됨
- union
	root가 다르면 root바로 밑으로 합병
'''