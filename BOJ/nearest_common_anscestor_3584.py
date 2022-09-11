#nearest_common_anscestor_3584.py
def	get_root_node(tree, node_cnt):
	root_candi = [ 0 for node in range(node_cnt + 1)]
	# print(f"{tree=}")
	for child_list in tree:
		for child_node in child_list:
			root_candi[child_node] += 1
	# print(f"{root_candi=}")
	for idx, cnt in enumerate(root_candi[1:]):
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
	abs_path = []
	while (stack and target_list):
		print(f"{stack=}")
		pop_node = stack.pop()
		print(f"{abs_path=}")
		print(f"{pop_node=}")
		abs_path.append(pop_node)
		if pop_node in target_list:
			target_list.remove(pop_node)
			abs_path_list.append(abs_path)
		elif tree[pop_node] == [] \
			or visited_list[pop_node] == False:
			abs_path.pop()
		elif visited_list[pop_node] == True:
			stack += tree[pop_node]
			visited_list[pop_node] = False
	print(f"{abs_path_list=}")
	# abs_path_list
