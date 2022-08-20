# 7569 tomato 3d
from collections import deque
cols, rows, heights = map(int ,input().split())
visited = [[[True for _ in range(cols)] for _ in range(rows)] for _ in range(heights) ]
distance = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(heights) ]
tomatoes_box = []
ripe_tomatoes_list =[]
for k in range(heights):
	tomatoes_layer = []
	for i in range(rows):
		tomatoes_row = list(map(int, input().split()))
		for j, tomatoes in enumerate(tomatoes_row):
			if tomatoes == 1:
				ripe_tomatoes_list.append((k,i,j))
		tomatoes_layer.append(tomatoes_row)
	tomatoes_box.append(tomatoes_layer)

# print(f"{tomatoes_box=}")
# print(f"{ripe_tomatoes_list=}")
queue = deque(ripe_tomatoes_list)
# print(f"{queue=}")
max_dis = 0
while (queue):
	z,x,y = queue.popleft()
	dx = [1, 0, -1, 0, 0, 0]
	dy = [0, 1, 0, -1, 0, 0]
	dz = [0, 0, 0, 0, 1, -1]
	for direc_x, direc_y, direc_z in zip(dx, dy, dz):
		adj_x, adj_y, adj_z = x + direc_x, y + direc_y, z + direc_z
		if 0 <= adj_x < rows and\
			0 <= adj_y < cols and\
			0 <= adj_z < heights and \
			tomatoes_box[adj_z][adj_x][adj_y] == 0:
			tomatoes_box[adj_z][adj_x][adj_y] = 1
			queue.append((adj_z, adj_x, adj_y))
			# print(f"{adj_x=} {adj_y=} {adj_z=}")
			visited[adj_z][adj_x][adj_y] = False
			distance[adj_z][adj_x][adj_y] = distance[z][x][y] + 1
			if max_dis < distance[adj_z][adj_x][adj_y]:
				max_dis = distance[adj_z][adj_x][adj_y]

def check_tomatoes(board):
	for k in range(heights):
		for i in range(rows):
			for j in range(cols):
				if board[k][i][j] == 0:
					return (-1)
	return (1)

# print(f"{tomatoes_box=}")
if check_tomatoes(tomatoes_box) == -1:
	print(-1)
else:
	print(max_dis)

'''
# 문제이해
토마토가 익는데 며칠 걸리는가?

생토마토는 익은 토마토가 주변에 있어야만 1일 뒤에 익는다.
토마토가 층을 져서 쌓여있다.
익으려면 2D 4방향(동서남북) 3D 위, 아래 총 6방향이 필요하다.


# 문제 해결방법
6방향 bsq
visited 필요?


# 검증


# 실행


# 회고 
'''
