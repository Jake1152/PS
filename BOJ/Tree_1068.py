# 1068 Tree.py

'''
- 삭제될 노드를 찾는다.
- 해당 노드에 단말노드를 찾아서 [-1]로 업데이트한다.
 이후 return
'''

def recursive_remove(be_removed_node, node_dict):
	for key, value in node_dict.items():
		if key == be_removed_node:
			for node in value:
				recursive_remove(node, node_dict)
			node_dict[key] = [-1]

n = int(input())
parent_node_list = list(map(int, input().split()))
be_removed_node = int(input())
node_dict = { node:[] for node in range(n)}

root_node = -1
# dict에 자식 노드들 추가
for cur_node, parent_node in enumerate(parent_node_list):
	if parent_node != -1:
		node_dict[parent_node].append(cur_node)
	else:
		root_node = cur_node

# print(f"{node_dict=}")
# if root_node == -1:
# 	print("error")
# 	# error처리
# else:
recursive_remove(be_removed_node, node_dict)
# be_removed_node 자식을 갖고 있던 리스트에서 해당 element제거
for key, sub_node_list in node_dict.items():
	for node in sub_node_list:
		if node == be_removed_node:
			sub_node_list.remove(node)

# print(f"{node_dict=}")

# counting leaf node
leaf_node_cnt = 0
for sub_node_list in node_dict.values():
	if sub_node_list == []:
		leaf_node_cnt += 1

print(leaf_node_cnt)

'''
트리가 이진트리라는 보장은 없다.
각 노드별로 리스트를 갖으며 그 리스트에는 자식노드가 담긴다.
없다면 그것이 리프노드

1. 트리구성
각 노드의 자식 노드를 리스트에 담는다.
그런식으로 순회한다.
dict안에 list를 담는다.

2. 삭제될 노드 탐색 및 제거
- 재귀
2번 
= [-1]

3. 리프노드 카운팅

노드가 0부터 시작이니 dict를 안쓰고
list로했어도 헷갈리는 부분없이 됐을거 같다.
'''