# firefly 3020

'''
1, 2, 3, 4, 5

- target == 4
try 
1. start = 1, end = 5, mid == 3
2. start = 4, end = 5, mid == 4
3. start = 5, end = 5, mid == 5
4. start = 5, end = 4, done!!!

- target == 2
1. start = 1, end = 5, mid == 3
2. start = 1, end = 2, mid == 1
3. start = 2, end = 2, mid == 2
4. start = 5, end = 4, done!!!
'''

def bin_search(arr_list ,start, end, target):
	while (start <= end):
		mid = (start + end) // 2
		if (arr_list[mid - 1] <= target):
			start = mid + 1
		else:
			end = mid - 1
	return (end)

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
sum_height = []
for x, y in zip(bottom, top):
	sum_height.append(x + y)

the_idx = bin_search(sum_height, 0, cave_length//2, cave_height)
print(f"{bottom=}")
print(f"{top=}")
print(f"{sum_height=}")
print(f"{the_idx=}")






'''
- 한쪽은 오름차순, 다른 한쪽은 내림차순으로 만든다.
- top은 오름차순
- bottom은 내림차순으로한다.

'''