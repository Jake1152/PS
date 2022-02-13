# connected element count 11724


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

parent = list(set(parent))
print(len(parent)-1)
# print(f"{parent=}")



'''
0 1 2 3
5 4 7 6
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