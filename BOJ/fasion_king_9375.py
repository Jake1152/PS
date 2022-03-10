# 9375 fasion king
from collections import defaultdict
test_case = int(input())
for _ in range(test_case):
	wearable = defaultdict(set)
	wearable_cnt = int(input())
	for _ in range(wearable_cnt):
		item, item_speices = input().split()
		wearable[item_speices].add(item)
	result = 1
	for key in wearable.keys():
		result *= (len(wearable[key]) + 1)
	print(result-1)