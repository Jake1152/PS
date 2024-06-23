event_count, event_relation_count = list(map(int, input().split()))

event_graph_dict = { num : { "descendant": set(), "ancestor": set()} for num in range(1, event_count + 1) }

print(f"{event_graph_dict=}")


'''
나의 조상인지 확인한다
어떻게?
재귀로?

new_node를 조상들 중에 나의 조상이 있는가?
같은 뿌리인지 확인한다.

union find? 서로 간의 순서는 알 수 없다
'''
def is_this_thing_my_ancestor(cur_node, new_node):
    # cur_node_ancestor_set = set().add(event_graph_dict[cur_node]["ancestor"])
    cur_node_ancestor_set = set().add(event_graph_dict[cur_node]["ancestor"])
    new_node_ancestor_set = set().add(event_graph_dict[new_node]["ancestor"])
    while (event_graph_dict[cur_node]["ancestor"] \
            or event_graph_dict[new_node]["ancestor"]):
        for node in event_graph_dict[cur_node]["ancestor"]:
            cur_node_ancestor_set.add(event_graph_dict[node]["ancestor"])
        for node in event_graph_dict[new_node]["ancestor"]:
            new_node_ancestor_set.add(event_graph_dict[new_node]["ancestor"])
        event_graph_dict[new_node]["ancestor"] 
        if (True):
            break
    return True

'''
새로 추가될 자손의 조상 중에 나의 조상과 겹치면 
새로 추가될 노드의 조상에서 나의 조상을 제거하고 내가 대신 들어간다. 
또한, 나의 조상 노드에서 새로 추가될 자손 노드를 조상 노드의 자손 목록에서 제거한다.

1. 자손 노드의 조상이 나의 조상과 겹치는지 확인한다.
   search_relation() 실행
2. 겹치다면,
  -1 자손 노드의 조상노드에서 자손 목록에 있는 새로운 자손 노드를 지운다.
    3 -> 1 
    1 -> 2, 3
    1 -> 2 

    3 -> 2

    # 1 -> 2 -> 3

  -2 자손 노드의 조상노드 목록에서 나의 조상을 지운다.

e.g) 100-43-23-11 -> 2
     1 -> 3
     1 -> 2

    1: ansetor: None
       desc: 2, 3
    2: ans: 1
    3: ans: 1

    1 - 2
    1 - 3
    2->3

     2 -> 3
     To be=>  1->2->3
'''
def connect_relation(ancestor, descendant) -> None:
    event_graph_dict[ancestor]["descendant"].add(descendant)
    event_graph_dict[descendant]["ancestor"].add(ancestor)


'''
조상이 겹치는지 어떻게 알것인가?

조상이 겹치더라도 순서는 어떻게 알 것인가?
둘의 조상을 거슬러 올라가며 서로가 나오는지 확인한다.
조상 중에 있다면 
상대방이 조상으로 있는 쪽이 후손이다.
e.g) lhs의 조상으로 rhs가 있다면 rhs가 더 먼저 나왔다.
둘다 겹치는 조상이 없다면 연관이 없다.
'''
def search_relation(relation_lhs, relation_rhs) -> int:
    return -1

for _ in range(event_relation_count):
    ancestor, descendant = list(map(int, input().split()))
    connect_relation(ancestor, descendant)

test_case_count = int(input())
for _ in range(test_case_count):
    relation_lhs, relation_rhs = list(map(int, input().split()))

    search_result = search_relation(relation_lhs, relation_rhs)
    print(search_result)