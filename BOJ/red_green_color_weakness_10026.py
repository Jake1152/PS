# 10026 red-green color weakness
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(board, visited_board, row, col):
	# 동북서남
	dx = [1, 0 , -1, 0]
	dy = [0, 1 , 0, -1]
	color_type = board[row][col]
	visited_board[row][col] = True
	for x, y in zip(dx, dy):
		if (0 <= row + x < square_size \
				and 0 <= col + y < square_size) \
			and visited_board[row + x][col + y] == False \
			and board[row + x][col + y] == color_type:
				dfs(board, visited_board, row + x, col + y)

square_size = int(input())
rg_square = []
visited = [ [False for _ in range(square_size)] for _ in range(square_size) ]
for _ in range(square_size):
	rg_square.append(list(input()))

rg_cnt = 0
for row in range(square_size):
	for col in range(square_size):
		if visited[row][col] == False:
			dfs(rg_square, visited, row, col)
			rg_cnt = rg_cnt + 1

# init visited for searching rg_weakness_square
visited = [ [False for _ in range(square_size)] for _ in range(square_size) ]
rg_weakness_cnt = 0
rg_weakness_square = [ ['R' if rg_square[x][y] == 'G' else rg_square[x][y]  for y in range(square_size)] for x in range(square_size) ]
for row in range(square_size):
	for col in range(square_size):
		if visited[row][col] == False:
			dfs(rg_weakness_square, visited, row, col)
			rg_weakness_cnt = rg_weakness_cnt + 1

print(" ".join([str(rg_cnt), str(rg_weakness_cnt)]))
