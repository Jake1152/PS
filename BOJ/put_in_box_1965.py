from sys import stdin
input = stdin.readline
n = int(input())
arr =[0]
arr += list(map(int, input().split()))
dy = [0]*(n+1)
dy[1] = 1
res = 0
for i in range(2, n+1):
	max = 0
	for j in range(i-1, 0, -1):
		if arr[j] < arr[i] and dy[j] > max:
			max = dy[j]
		dy[i] = max + 1
		if dy[i] > res:
			res = dy[i]
print(res)