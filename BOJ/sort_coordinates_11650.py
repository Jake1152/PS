from sys import stdin
input = stdin.readline
n = int(input())
coordinates = []
for _ in range(n):
	x, y = map(int, input().split())
	coordinates.append((x, y))

for x, y in sorted(coordinates, key=lambda coordi: (coordi[0], coordi[1])):
	print(' '.join([str(x), str(y)]))
