# 1966 printer queue
from collections import deque
t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	s = deque(map(int, input().split()))
	s_posi = deque([0 for i in range(n)])
	s_posi[m] = 1
	cnt = 0
	while True:
		if s[0] == max(s):
			cnt += 1
			if s_posi[0] == 1:
				print(cnt)
				break
			else:
				s.popleft()
				s_posi.popleft()
		else:
			s.append(s[0])
			s.popleft()
			s_posi.append(s_posi[0])
			s_posi.popleft()

'''
from collections import deque
t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	queue = deque()
	org_queue = deque((map(int, input().split())))
	print(f"{org_queue=}")
	# find_num = org_queue[m]



'''