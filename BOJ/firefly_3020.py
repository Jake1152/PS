# firefly 3020

def binsearch():
	pass


cave_length, cave_height = list(map(int, input().split()))
top = []
bottom = []
for idx in range(cave_length):
	if (idx % 2):
		bottom.append(int(input()))
	else:
		top.append(int(input()))

bottom.sort(reverse=True)
top.sort()





'''
- 한쪽은 오름차순, 다른 한쪽은 내림차순으로 만든다.
- top은 오름차순
- bottom은 내림차순으로한다.

'''