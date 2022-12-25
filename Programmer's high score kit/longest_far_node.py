from collections import deque
def solution(n, edge):
    distance = [ 0 for _ in range (n + 1)]
    adjacent_list = [ [] for _ in range(n + 1) ]
    prev_node_list = [ 0 for _ in range(n + 1) ]
    for begin_node, end_node in edge:
        adjacent_list[begin_node].append(end_node)
        adjacent_list[end_node].append(begin_node)
        prev_node_list[end_node] = begin_node
        if prev_node_list[begin_node] == 0:
            prev_node_list[begin_node] = end_node
    visited = [ False for _ in range(n + 1) ]
    queue = deque([1])
    prev_node = 1
    print(f"{adjacent_list=}")
    while (queue):
        print(f"{queue=}")
        node = queue.popleft()
        print(f"{node=}")
        # print(f"{visited=}")
        if visited[node] == False:
            visited[node] = True
            queue += adjacent_list[node]
            if node == 1:
                continue
            prev_node = prev_node_list[node]
            print(f"{prev_node=}")
            distance[node] += distance[prev_node] + 1
            print(f"{distance=}")
    max_value = max(distance)
    print(f"{distance=}")
    answer = 0
    for node_distance in distance:
        if node_distance == max_value:
            answer += 1
    return answer


n = 6
vectex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(f"{solution(n, vectex)=}")

'''
#문제이해
- 1번 노드에서 가장 거리가 먼 노드의 개수

#문제 해결방법
- 1번 노드부터 순회 필요 
- 각 노드별로 거리를 기록

'''