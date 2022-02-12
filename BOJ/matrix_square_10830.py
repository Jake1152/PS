# 10830 matrix square
from sys import stdin
input = stdin.readline


def matrix_square(a_matrix, b_matrix):
	for i in range(N):
		for j in range(N):
			element_calculate_result = 0
			for k in range(N):
				element_calculate_result += (a_matrix[i][k] * b_matrix[k][j])
			result_matrix[i][j] = element_calculate_result % 1000
	return result_matrix


def matrix_square_recursion(a_matrix, b_matrix, power):
	if (power < 2):
		return matrix_square(a_matrix, b_matrix)

		
	pass


N, B = map(int, input().split())
matrix = []
for _ in range(N):
	matrix.append(list(map(int, input().split())))
result_matrix = [[ matrix[i][j] for j in range(N)] for i in range(N)]
multiple_matrix = [[ matrix[i][j] for j in range(N)] for i in range(N)]
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