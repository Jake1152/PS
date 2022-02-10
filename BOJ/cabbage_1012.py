# 유기농 배추 1012
import sys
sys.setrecursionlimit(10**6)

def dfs(field, x, y, N, M):
	field[x][y] = 2
	dx = [1, 0, -1, 0]
	dy = [0, -1, 0, 1]
	for i, j in zip(dx, dy):
		row = i + x
		col = j + y
		if 0 <= row < N and 0 <= col < M:
			if field[row][col] == 1:
				dfs(field, row, col, N, M)

T = int(input())
for _ in range(T):
	M, N, K = map(int, input().split())
	field = [ [ 0 for _ in range(M)] for _ in range(N) ]
	cnt = 0
	for _ in range(K):
		y, x = map(int ,input().split())
		field[x][y] = 1
	for i in range(N):
		for j in range(M):
			if (field[i][j] == 1):
				dfs(field, i, j, N, M)
				cnt += 1
	print(cnt)
	