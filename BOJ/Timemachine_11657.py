#Timemachine_11657
city_cnt, bus_path_cnt = map(int, input().split())
city_dict = { city_node : [] for city_node in range(1, city_cnt + 1) }
print(f"{city_dict=}")
for _ in range(bus_path_cnt):
    start_city, end_city, cost = map(int, input().split())
    city_dict[start_city].append()
    city_dict[end_city].append()
    # (start, end, cost)

'''

for i in range(n-1): # edge cnt
    for each edge(u, v) in G:
        if dist[v] > dist[u] + w(u,v):
            relax(u, v) # relax is update!
n**2
최악의 경우 n**3

edge수가 노드수의 제곱만큼이다.

n**2 * n => n**3


노드 4개 
4 * 3
하나의 정점에 이어질수 있는 간선의 수 3*2개

n*(n-1) // 2 * 1
(n**2 - n) // 2

n**2

ployd washall

n**3

- 다익스트라
    - 현재에서 최소만봄
- 벨만포드
    - bruteforce처럼

'''

