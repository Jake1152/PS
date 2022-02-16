def chk_biggest_block(board, size):
	global g_block_size

	for i in range(size):
		for j in range(size):
			if g_block_size < board[i][j]:
				g_block_size = board[i][j]

def cp_board(board, size):
	new_board = [ [ board[i][j] for j in range(size) ] for i in range(size) ]
	# print(f"{new_board=}")
	return (new_board)

def east_direc(board, size):
	# print("## east_direc")
	# 열우선 오른쪽 열부터 확인 
	merge_cnt = 0
	for col in range(size - 1, 0, -1):
		for row in range(size):
			# 맨오른쪽 열이 비어있는 경우 왼쪽 열에서 가져와서 채운다(값이 있다면)
			if board[row][size - 1] == 0:
				for beside_col in range(col - 1, -1, -1):
					if  board[row][beside_col] != 0:
						board[row][size - 1] = board[row][beside_col]
						board[row][beside_col] = 0
						break

			for beside_col in range(col - 1, -1, -1):
				if board[row][beside_col] == board[row][col]:
					board[row][col] *= 2
					merge_cnt += 1
					board[row][beside_col] = 0
				elif board[row][beside_col] != 0:
					if (col - 1) != beside_col:
						board[row][col - 1] = board[row][beside_col]
						board[row][beside_col] = 0
				else: # 옆에 열의 값이 0일때 
					continue				
				break
	# print(f"{board=}")
	return merge_cnt

def west_direc(board, size):
	# print("## west_direc")
	# print(f"start of method {board=}")
	merge_cnt = 0
	# 열우선 왼쪽 열부터 확인 
	for col in range(0, size - 1):
		for row in range(size):
			# 맨왼쪽 열이 비어있는 경우 오른쪽 열에서 가져와서 채운다(값이 있다면)
			if board[row][0] == 0:
				# print(f"{board=}")
				# print(f"{row=}")
				# print(f"{col=}")
				for beside_col in range(col + 1, size):
					if  board[row][beside_col] != 0:
						board[row][0] = board[row][beside_col]
						board[row][beside_col] = 0
						break
			# print(f"after left side was 0 {col=} {row=} {board=}")
			for beside_col in range(col + 1, size):
				if board[row][beside_col] == board[row][col]:
					board[row][col] *= 2
					board[row][beside_col] = 0
					merge_cnt += 1
				elif board[row][beside_col] != 0:
					if (col - 1) != beside_col:
						board[row][col - 1] = board[row][beside_col]
						board[row][beside_col] = 0
				else: # 옆에 열의 값이 0일때 
					continue
				break
	# print(f"{board=}")
	return merge_cnt

def south_direc(board, size):
	# print("## south_direc")
	merge_cnt = 0
	# 행우선 맨 아래 행부터 확인 
	for row in range(size - 1, 0, -1):
		for col in range(size):
			# 맨아래 행이 비어있는 경우 위쪽 행에서 가져와서 채운다(값이 있다면)
			if board[size - 1][col] == 0:
				for beside_row in range(row - 1, -1, -1):
					if  board[beside_row][col] != 0:
						board[size - 1][col] = board[beside_row][col]
						board[beside_row][col] = 0
						break

			for beside_row in range(row - 1, -1, -1):
				if board[beside_row][col] == board[row][col]:
					board[row][col] *= 2
					board[beside_row][col] = 0
					merge_cnt += 1  
				elif board[beside_row][col] != 0:
					if (row - 1) != beside_row:
						board[row - 1][col] = board[beside_row][col]
						board[beside_row][col] = 0
				else: # 옆에 행의 값이 0일때 
					continue
				break
	# print(f"{board=}")
	return merge_cnt

def north_direc(board, size):
	# print("## north_direc")
	merge_cnt = 0
	# 행우선 맨 위 행부터 확인 
	for row in range(0, size - 1):
		for col in range(size):
			# 맨 위 행이 비어있는 경우 아래쪽 행에서 가져와서 채운다(값이 있다면)
			if board[0][col] == 0:
				for beside_row in range(row + 1, size):
					if  board[beside_row][col] != 0:
						board[0][col] = board[beside_row][col]
						board[beside_row][col] = 0
						break

			for beside_row in range(row + 1, size):
				if board[beside_row][col] == board[row][col]:
					board[row][col] *= 2
					board[beside_row][col] = 0
					merge_cnt += 1
				elif board[beside_row][col] != 0:
					if (row - 1) != beside_row:
						board[row - 1][col] = board[beside_row][col]
						board[beside_row][col] = 0
				else: # 옆에 행의 값이 0일때 
					continue
				break
	# print(f"{board=}")
	return merge_cnt

def dfs(direction, level, board, size):
	global g_cnt
	if (level == 5):
		chk_biggest_block(board, size)
		# print("level in dfs: ", level)
		# print("board in dfs: ", board)
		g_cnt += 1
		return
	merge_cnt = 0
	direc_flag = ""
	if direction == "e":
		merge_cnt = east_direc(board, size)
		direc_flag = "e"
	elif  direction == "w":
		merge_cnt = west_direc(board, size)
		direc_flag = "w"
	elif  direction == "s":
		merge_cnt = south_direc(board, size)
		direc_flag = "s"
	elif  direction == "n":
		merge_cnt = north_direc(board, size)
		direc_flag = "n"

	for direc in ("e", "w", "s", "n"):
		# print(f"{direc=}")
		new_board = cp_board(board, size)
		if (merge_cnt == 0) and (direc == direc_flag):
			continue
		dfs(direc, level + 1, new_board, size)

g_block_size = 0
g_cnt = 0
size = int(input())
board = []

for _ in range(size):
	board.append(list(map(int, input().split())))

dfs("", 0, board, size)

print(g_block_size)
# print("g_cnt: ", g_cnt)
