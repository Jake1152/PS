# 11866 Josephus

# 1 2 3 4 5 6 7
#     1     2
from collections import deque

n, k = map(int, input().split())
circle = deque([str(i) for i in range(1, n+1)])
answer = []
while circle:
	for _ in range(k-1):
		circle.append(circle.popleft())
	answer.append(circle.popleft())
# print(f"{answer=}")
print("<"+ ", ".join(answer) + ">")
