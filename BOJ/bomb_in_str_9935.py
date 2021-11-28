# bomb in str 9935
from sys import stdin
from collections import deque

input = stdin.readline

normal_str = deque(input().split())
bomb_str = deque(input().split())

while True:
	if bomb_str in normal_str:
		normal_str = normal_str.replace(bomb_str, "")
	else:
		break

result = normal_str if normal_str else "FRULA"
print(result)