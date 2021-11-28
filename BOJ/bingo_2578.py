n = 5
board = []
check = []
#global line_cnt
#line_cnt = 0

for _ in range(n):
	board.append(list(map(int, input().split())))

for _ in range(n):	
	check += list(map(int, input().split()))

def count_bingo_line():
	#global line_cnt
	# 가로, 세로, 대각 한번에 확인 할수있는 방법은?
	line_cnt = 0
	for x in range(n):
		row_cnt = 0
		col_cnt = 0
		for y in range(n):
			if board[x][y] == 0:
				row_cnt += 1
			if board[y][x] == 0:
				col_cnt += 1
		if row_cnt == 5:
			line_cnt += 1
		if col_cnt == 5:
			line_cnt += 1
	# diagonal
	# 정가운데가 체크되었는지?
	if board[2][2] == 0:
		# 우하향 대각
		cnt = 0
		for l_d_i in range(5):
			if board[l_d_i][l_d_i] != 0:
				cnt += 1
		if cnt == 5:
			line_cnt += 1
		
		# 우상향 대각
		y = 0
		cnt = 0
		for x in range(4, -1, -1):
			if board[x][y] == 0:
				cnt += 1
			y += 1
		if cnt == 5:
			line_cnt += 1
		
	return line_cnt

def matching(val):
	for x in range(n):
		for y in range(n):
			if board[x][y] == val:
				board[x][y] = 0
	# print(f"{board=}")

for idx in range(len(check)):
	matching(check[idx])
	line_cnt = count_bingo_line()
	# print(f"{line_cnt=}")
	if line_cnt >= 3:
		print(idx+1)
		break
