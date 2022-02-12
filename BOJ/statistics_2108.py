#statistics 2108

'''
1. mean
2. median
3. mode
4. range
'''
from collections import Counter
from sys import stdin

input = stdin.readline
cnt = int(input())
num_list = []
statistics = []
for _ in range(cnt):
	num_list.append(int(input()))
num_list_len = len(num_list)
mean = round(sum(num_list)/num_list_len)
statistics.append(mean)
num_list.sort()
statistics.append(num_list[num_list_len//2])
count_num_list = Counter(num_list).most_common(2)
if count_num_list[0][1] == count_num_list[-1][1]:
	mode = count_num_list[-1][0]
else:
	mode = count_num_list[0][0]
statistics.append(mode)
arange = num_list[-1] - num_list[0]
statistics.append(arange)

for value in statistics:
	print(value)