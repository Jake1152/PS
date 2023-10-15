from collections import defaultdict

'''
- root_node를 기준으로 왼쪽, 오른쪽을 순회한다.
- 
'''
def can_I_go_there(cur_node, info, animal_farm):
    copy_animal_farm = {'sheep': animal_farm['sheep'], 'wolf': animal_farm['wolf']}
    if info[cur_node] == 0: # sheep
        copy_animal_farm['sheep'] += 1
    else:
        copy_animal_farm['wolf'] += 1
    diff = copy_animal_farm['sheep'] - copy_animal_farm['wolf']
    if (diff < 1):
        return False
    return True

def dfs(root_node, tree, info, acc):
    if info[root_node] == 0:
        acc += 1
    for cur_node in tree[root_node]['child']:
        acc = dfs(cur_node, tree, info, acc)
    return acc
'''
단지 서브 트리에 양이 있는지만 확인한다
몇마리인지, 거기까지 갈만한지는 확인하지 않는다.
'''
def is_there_any_other_sheep(cur_node, tree, info):
    if dfs(cur_node, tree, info, 0) > 0:
        return True
    return False

'''
tree = {node{parent: int , child: [int, int]}, ..., node{parent: int , child: [int, int]}}
tree->node->(parent or child)
'''
def make_tree(edges):
    tree = defaultdict(dict)
    for cur_node_info in edges:
        cur_node, child_node = cur_node_info
        if tree.get(cur_node) == None:
            tree[cur_node] = {'parent':None, 'child': []}
        tree[cur_node]['child'].append(child_node)
        if tree.get(child_node) == None:
            tree[child_node] = {'parent':None, 'child': []}
        tree[child_node]['parent'] = cur_node
    return tree

def solution(info, edges):
    global animal_farm
    sorted_edges = sorted(edges, key = lambda x : x[0])
    visited = [False for _ in range(len(info))]
    tree = make_tree(sorted_edges)
    print(f"{tree=}")
    print(f"{is_there_any_other_sheep(0, tree, info)=}")

    animal_farm = {'sheep': 0, 'wolf': 0}
    for cur_node in tree:
        can_I_go_there(cur_node, info, animal_farm)

    # print(f"{animal_farm=}")

    return animal_farm['sheep']

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

# info = [0,1,0,1,1,0,1,0,0,1,0]
# edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

print(f"{solution(info, edges)=}")