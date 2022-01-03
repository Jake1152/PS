
def check_sqaure_vertex(eleven_bound_idx, gap):
	row, col = eleven_bound_idx
	vertex_value = g_rectangle[row][col]
	'''
	(x,y)				(x, y+square_size)
	(x+square_size,y)	x+square_size, y+square_size)
	'''
	dx = [0, gap, gap]
	dy = [gap, 0, gap]
	for i in range(3):
		x = row + dx[i]
		y = col + dy[i]
		if (x < g_N and y < g_M):
			# print(f"{x=}, {y=}")
			if g_rectangle[x][y] != vertex_value:
				return (False)
	return (True)
	
def find_square():
	square_side = max(g_N, g_M)
	while (square_side > 1):
		'''
		꼭지점 찾는 루틴routine
		'''
		for row in range(g_N - square_side + 1):
			for col in range(g_M - square_side + 1):
				if check_sqaure_vertex((row, col), square_side-1):
					return square_side
		square_side -= 1
	return (square_side)	

g_N, g_M = map(int, input().split())
g_rectangle = []
for _ in range (g_N):
	g_rectangle.append(list(map(int, list(input()))))
# print(f"{g_rectangle=}")
square_side = find_square()
print(square_side ** 2)
