# 10830 matrix square
from sys import stdin
input = stdin.readline

def multiply_matrix(a_matrix, b_matrix):
	return_matrix = [[0 for j in range(N)] for i in range(N)]
	for i in range(N):
		for j in range(N):
			element_calculate_result = 0
			for k in range(N):
				element_calculate_result += (a_matrix[i][k] * b_matrix[k][j])
			return_matrix[i][j] = element_calculate_result % 1000
	return return_matrix

def matrix_square(matrix):
	return_matrix = [[0 for j in range(N)] for i in range(N)]
	for i in range(N):
		for j in range(N):
			element_calculate_result = 0
			for k in range(N):
				element_calculate_result += (matrix[i][k] * matrix[k][j])
			return_matrix[i][j] = element_calculate_result % 1000
	return return_matrix

def matrix_moduler(base_matrix):
	for i in range(N):
		for j in range(N):
			base_matrix[i][j] = base_matrix[i][j] % 1000
	return base_matrix

def matrix_square_recursion(base_matrix, power):
	if (power == 1):
		return matrix_moduler(base_matrix)
	current_square_matrix = matrix_square_recursion(base_matrix, power//2)
	if power % 2 == 0:
		return matrix_square(current_square_matrix)
	return multiply_matrix(matrix_square(current_square_matrix), org_matrix)

N, power_cnt = map(int, input().split())
matrix = []
org_matrix = []
for _ in range(N):
	matrix.append(list(map(int, input().split())))
for row_vector in matrix:
	org_matrix.append(row_vector)

result_matrix = matrix_square_recursion(matrix, power_cnt)
for i in range(N):
	for j in range(N):
		print(result_matrix[i][j],  end=' ')
	print()
'''

# 행렬을  B번 제곱한다.
for times in range(2, B+1):
	# 행렬 곱
	for i in range(N):
		for j in range(N):
			element_calculate_result = 0
			for k in range(N):
				element_calculate_result += (multiple_matrix[i][k] * matrix[k][j])
			result_matrix[i][j] = element_calculate_result % 1000
	multiple_matrix = [[ result_matrix[i][j] for j in range(N)] for i in range(N)]
for i in range(N):
	for j in range(N):
		print(result_matrix[i][j],  end=' ')
	print()


2 1
1000 1000
1000 1000
0 0
0 0

3 999
1 2 3
4 5 6
7 8 9
'''