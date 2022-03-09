#16928 snake and ladder game
from collections import deque
board = [i for i in range(101)]
visited = [True for _ in range(101)]
distance = [0 for i in range(101)]
portal_entrance_list = []
portal_exit_list = []
def bfs():
	queue = deque([1])
	while queue:
		cur_num = queue.popleft()
		visited[cur_num] = False
		if cur_num == 100:
			return 
		# print(f"{cur_num=}")
		for num in range(1, 7):
			next_num = cur_num + num
			if next_num <= 100 and visited[next_num]:
				if distance[next_num] == 0 or distance[next_num] > distance[cur_num] + 1:
					distance[next_num] += distance[cur_num] + 1
				if next_num in portal_entrance_list:
					idx = portal_entrance_list.index(next_num)
					visited[next_num] = False
					next_num = portal_exit_list[idx]
					if distance[next_num] == 0 or distance[next_num] > distance[cur_num] + 1:
						distance[next_num] += distance[cur_num] + 1
					queue.append(portal_exit_list[idx])
				else:
					queue.append(next_num)

ladder_cnt, snake_cnt = map(int, input().split())
for _ in range(ladder_cnt+snake_cnt):
	entrance_posi, exit_posi = map(int, input().split())
	portal_entrance_list.append(entrance_posi)
	portal_exit_list.append(exit_posi)

bfs()
# print(distance)
print(distance[100])

'''
#문제이해
10*10크기 보드
bfs, 다른점은 4방향이 아니라 주사위 숫자를 더해서 이동하며 뱀,사다리라는 별도의 통로가 있어서
다른 곳으로 이동 될 수 있다.
시작위치는 1, 목적지는 100번칸

#문제재정의
변형된 bfs
시작점과 목적지는 고정되어있다.
지름길 혹은 뒤로 가는 경우가 있다.

#문제해결방법
bfs로 해결한다.
최적화를 할수 있는 부분도 있을것같지만 그런부분은 고려하지 않는다.
한다면 최적화룰이 촘촘해야할거 같다.

10*10 board, visited, distacne
사다리, 뱀 list input
1번 칸부터 주사위를 굴리면서 100번칸까지 간다.
중간에 사다리 뱀이면 그곳으로 점프된다.
방문한곳은 visited에 표시하며 distance에서는 이전 위치에서 +1한다.

그런데 문제가 
어떤 순서로 방문하느냐에 따라서 달라질수 있을것 같다
그런부분들은 어떻게 해결할 수 있는가?

#검증


#실행


#회고




'''