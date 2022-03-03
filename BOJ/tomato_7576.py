#tomatoes_7576
from sys import stdin

input = stdin.readline

def search():
	global org_board
	new_board = [ [0 for _ in range(cols)] for _ in range(rows) ]
	copy_board(new_board, org_board)
	# 4 direc bounds
	dx = [0, 1, 0, -1]
	dy = [1, 0, -1, 0]
	for x in range(rows):
		for y in range(cols):
			# 현재가 안익어 있다면
			if org_board[x][y] == 0:
				# 주변에 익은 토마토가 있는지 4방향 탐색
				for step_x, step_y in zip(dx, dy):
					if 0 <= x + step_x < rows and 0 <= y + step_y < cols and\
						org_board[x + step_x][y + step_y] == 1:
						new_board[x][y] = 1
						break 
	# 다 끝나면 다시 원본 board를 갱신
	copy_board(org_board, new_board)


def check_tomatoes(board):
	global g_tomatoes_status
	# cur_tomatoes_status
	ripe_tomatoes, unripe_tomatoes = 0, 0
	for i in range(rows):
		for j in range(cols):
			if board[i][j] == 1:
				ripe_tomatoes += 1
			elif board[i][j] == 0:
				unripe_tomatoes += 1
	prev_ripe_tomatoes, prev_unripe_tomatoes = g_tomatoes_status
	if (ripe_tomatoes == prev_ripe_tomatoes and \
		unripe_tomatoes == prev_unripe_tomatoes):
		if unripe_tomatoes > 0:
			return (-1)
		return (0)
	g_tomatoes_status = [ripe_tomatoes, unripe_tomatoes]
	return (1)

def copy_board(new_board, prev_board):
	for i in range(rows):
		for j in range(cols):
			new_board[i][j] = prev_board[i][j]

cols, rows = map(int, input().split())
org_board = []
for _ in range(rows):
	org_board.append(list(map(int, input().split())))

# print(f"{org_board=}")
g_days = 0
g_tomatoes_status = [0, 0]
check_tomatoes(org_board)
while (True):
	search()
	flag = check_tomatoes(org_board) 
	if (flag <= 0):
		if flag == -1:
			g_days = -1
		break
	g_days += 1

print(g_days)