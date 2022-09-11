#nearest_common_anscestor_3584.py
def	get_root_node(tree, node_cnt):
	root_candi = [ 0 for node in range(node_cnt + 1)]
	for child_list in tree:
		for child_node in child_list:
			root_candi[child_node] += 1
	for idx, cnt in enumerate(root_candi):
		if cnt == 0:
			return idx + 1
	return -1

def	get_target_path():
	pass

test_cnt = int(input())
for _ in range(test_cnt):
	abs_path_list = []
	node_cnt = int(input())
	# node 숫자가 1부터이므로 0번은 dummy list를 놔둔다.
	tree = [ [] for _ in range(node_cnt + 1)]
	visited_list = [ True for _ in range(node_cnt + 1)]
	for _ in range(node_cnt - 1):
		parent_node, child_node = map(int, input().split())
		tree[parent_node].append(child_node)
	root_node = get_root_node(tree, node_cnt)
	if root_node == -1:
		print("there are no root.")
	target_list = list(map(int, input().split()))
	# root
	# search
	stack = [root_node]
	while (True):
		parent_node = stack[-1]
		for child_list in tree[parent_node]:
			for node in child_list:
				if visited_list[node] == True:
					visited_list[node] = False
					# find target
					if node in target_list:
						target_list.remove(node)
						abs_path_list.append(stack)
					
	
