paper_cnt_dict = {-1: 0, 0: 0, 1: 0}

# 정사각형이 같은 값으로 이루어졌는지 같다면 해당 dict에서 증가하며 True return 아니면 False
def check_square(x, y, side):
	standard_num = paper_matrix[x][y]
	for i in range(x, x+side):
		for j in range(y, y+side):
			if standard_num != paper_matrix[i][j]:
				return (False)
	paper_cnt_dict[stzandard_num] += 1
	return (True)

def count_paper(x, y, side):
	'''
	1. 영역이 같은지 확인
	2. 다르면 9등분 한뒤 count_paper() 호출(각 왼쪽상단 꼭지점을 보냄)
	'''
	if check_square(x, y, side) == True:
		return 
	else:
		# 9등분
		## 0
		count_paper(x, y, side//3)
		count_paper(x, y+side//3, side//3)
		count_paper(x, y+2*(side//3), side//3)
		## 1/3지점 
		count_paper(x+side//3, y, side//3)
		count_paper(x+side//3, y+side//3, side//3)
		count_paper(x+side//3, y+2*(side//3), side//3)
		## 2/3지점 
		count_paper(x+2*(side//3), y, side//3)
		count_paper(x+2*(side//3), y+side//3, side//3)
		count_paper(x+2*(side//3), y+2*(side//3), side//3)

square_side = int(input())
paper_matrix = []
for _ in range(square_side):
	paper_matrix.append(list(map(int, input().split())))

count_paper(0, 0, square_side)

# -1,0,1 종이 갯수 print
for val in paper_cnt_dict.values():
	print(val)