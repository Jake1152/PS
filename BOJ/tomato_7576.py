#tomatoes_7576
from sys import stdin
from collections import deque
input = stdin.readline
def append_tomatoes_to_deque(board):
	toms_queue = deque()
	for x in range(rows):
		for y in range(cols):
			if board[x][y] == 1:
				toms_queue.append((x,y))
	return toms_queue

def bfs(queue):
	global org_board
	visited = [[True for _ in range(cols)] for _ in range(rows)]
	new_board = copy_board(org_board)
	distance = [[0 for _ in range(cols)] for _ in range(rows)]
	max_dis = 0
	while (queue):
		x, y = queue.popleft()
		dx = [1, 0, -1, 0]
		dy = [0, 1, 0, -1]
		# search 4 direc
		for direc_x_, direc_y in zip(dx, dy):
			adj_x, adj_y  = x + direc_x_, y + direc_y
			if 0 <= adj_x < rows and 0 <= adj_y < cols and\
				org_board[adj_x][adj_y] == 0 and\
				new_board[adj_x][adj_y] == 0 and\
				visited[adj_x][adj_y]:
				visited[adj_x][adj_y] = False
				new_board[adj_x][adj_y] = 1
				queue.append((adj_x, adj_y))
				distance[adj_x][adj_y] = distance[x][y] + 1
				if max_dis < distance[adj_x][adj_y]:
					max_dis = distance[adj_x][adj_y]
	# print(f"{distance=}")
	org_board = new_board
	return max_dis

def check_tomatoes(board):
	for i in range(rows):
		for j in range(cols):
			if board[i][j] == 0:
				return (-1)
	return (1)

def copy_board(prev_board):
	new_board = [[0 for _ in range(cols)] for _ in range(rows)]
	for i in range(rows):
		for j in range(cols):
			new_board[i][j] = prev_board[i][j]
	return (new_board)
cols, rows = map(int, input().split())
org_board = []
for _ in range(rows):
	org_board.append(list(map(int, input().split())))

queue = append_tomatoes_to_deque(org_board)
days = bfs(queue)
# print(f"{org_board=}")
if check_tomatoes(org_board) == -1:
	print(-1)
else:
	print(days)

'''



def copy_board(new_board, prev_board):
	for i in range(rows):
		for j in range(cols):
			new_board[i][j] = prev_board[i][j]


'''