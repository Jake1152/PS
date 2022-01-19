# check square
def check_paper_color(x, y, N):
	standard_color = color_paper[x][y]
	for i in range(x, x + N):
		for j in range(y, y + N):
			if color_paper[i][j] != standard_color:
				return (-1)
	return (standard_color)

def div_conq(x, y, N):
	global blue_paper_cnt, white_paper_cnt, g_white, g_blue

	color_flag = check_paper_color(x, y, N)
	if color_flag == g_white:
		white_paper_cnt += 1
	elif color_flag == g_blue:
		blue_paper_cnt += 1
	else:
		div_conq(x, y, N // 2)
		div_conq(x + N // 2, y, N // 2)
		div_conq(x, y + N // 2, N // 2)
		div_conq(x + N // 2, y + N // 2, N // 2)

N = int(input())
color_paper = []
blue_paper_cnt = 0
white_paper_cnt = 0
g_white = 0
g_blue = 1
# 색종이 영역 추가
for _ in range(N):
	color_paper.append(list(map(int, input().split())))

# print(f"{color_paper=}")
div_conq(0, 0, N)
print(white_paper_cnt)
print(blue_paper_cnt)
