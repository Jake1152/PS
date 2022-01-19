from collections import deque

n = int(input())
queue = deque([i for i in range(1, n+1)])

remain = 1
while queue:
	remain = queue.popleft()
	queue.rotate(-1)

print(remain)
