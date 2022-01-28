#  coordinate sort2, 11651
from sys import stdin
input = stdin.readline
n = int(input())
coordinate_list = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinate_list.append((x, y))

for x, y in sorted(coordinate_list, key=lambda x:  (x[1], x[0])):
    print(x, y)