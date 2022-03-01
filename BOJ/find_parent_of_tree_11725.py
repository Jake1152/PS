import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def dfs(start, tree):
    # 부모노드 설정안된것 설정하고서 dfs진행
    for adj_node in tree[start]:
        if parent[adj_node] == 0:
            parent[adj_node] = start
            dfs(adj_node, tree)

n = int(input())
parent = [0 for _ in range(n+1)]
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a_node, b_node = map(int, input().split())
    tree[a_node].append(b_node)
    tree[b_node].append(a_node)

dfs(1, tree)
for node in range(2, n+1):
    print(parent[node])

'''

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return (parent[x])

def union_set(a_node, b_node):
    a_parent = find_set(a_node)
    b_parent = find_set(b_node)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent
        
n = int(input())
parent = [i for i in range(n+1)]
edges = []
for _ in range(n-1):
    from_node, to_node = map(int, input().split())
    edges.append([from_node, to_node])
print(f"{edges=}")
for from_node, to_node in edges:
    from_parent = find_set(from_node)
    print(f"{from_parent=}")
    to_parent = find_set(to_node)
    print(f"{to_parent=}")
    if from_parent != to_parent:
        union_set(from_node, to_node)
    print(f"{parent=}")

print(f"before loop {parent=}")

for node_idx in range(1, n + 1):
	parent[node_idx] = find_set(node_idx)

print(f"after loop {parent=}")
    
'''