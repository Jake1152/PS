# 10989 sort3
from sys import stdin

input = stdin.readline

N = int(input())
check_list = [0] * 10001

for _ in range(N):
	input_num = int(input())
	check_list[input_num] = check_list[input_num] + 1

for i in range(10001):
	if check_list[i] != 0:
		for _ in range(check_list[i]):
			print(i)