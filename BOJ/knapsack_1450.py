def dfs(level, limit, list, index):


g_count = 0
n, c = map(int, input().split())
tmp_items = list(map(int, input().split()))
items = []

for element in tmp_items:
	if c >= element:
		
		items.append(element)
sort(items)
sum = 0
max_count = 0
for element in items:
	sum += element
    max_count += 1
	if c < sum:
		max_count -= 1
        break
	elif c == sum
		break
