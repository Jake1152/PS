import sys
x=100
sys.setrecursionlimit(x)

N = int(input())
color_paper = []
blue_paper_cnt = 0
white_paper_cnt = 0

# check square
def check_paper_color(top_coordinate, bottom_coordinate):
	top_x, top_y = top_coordinate
	standard_color = color_paper[top_x][top_y]
	bottom_x, bottom_y = bottom_coordinate
	for x in range(top_x, bottom_x + 1):
		for y in range(top_y, bottom_y + 1):
			if color_paper[x][y] != standard_color:
				return (False)
	return True

# square quarter divide
def divide_paper_to_sqaure(top_coordinate, bottom_coordinate):
	coordinates = []
	top_x, top_y = top_coordinate
	bottom_x, bottom_y = bottom_coordinate
	# 영역 4등분하여 coordnates에 append
	# 2 사분면
	coordinates.append((top_coordinate, (bottom_x//2, bottom_y//2)))
	# 1 사분면
	coordinates.append(((top_x, bottom_y//2), (bottom_x//2, bottom_y)))
	# 3 사분면
	coordinates.append(((bottom_x//2, top_y), (bottom_x, bottom_y//2)))
	# 4 사분면
	coordinates.append(((bottom_x//2, bottom_y//2), (bottom_x, bottom_y)))

	return coordinates

def count_color_paper(top_coordinate, bottom_coordinate):
	global blue_paper_cnt, white_paper_cnt
	# exit case
	print(f"{top_coordinate=}")
	print(f"{bottom_coordinate=}")
	top_x, top_y = top_coordinate
	# 길이가 1이 되면
	if (top_coordinate[0] - bottom_coordinate[0] == 1):
		if (color_paper[top_x][top_y] == 1):
			blue_paper_cnt += 1
		else:
			white_paper_cnt += 1
		print("exit")
		return
	# 전체영역 확인
	if (check_paper_color(top_coordinate, bottom_coordinate)):
		# 색종이 색상 확인해서 counting
		if (color_paper[top_x][top_y] == 1):
			blue_paper_cnt += 1
		else:
			white_paper_cnt += 1
	# 다른 색상이 껴있으면 영역 4등분
	else:
		area_coordinates = divide_paper_to_sqaure(top_coordinate, bottom_coordinate)
		for top, bottom in area_coordinates:
			count_color_paper(top, bottom)

for _ in range(N):
	color_paper.append(list(map(int, input().split())))

count_color_paper((0, 0), (N, N))
print(blue_paper_cnt)
print(white_paper_cnt)
