#never heard before, never heard before 1764
import sys
from collections import defaultdict
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
people = defaultdict(int)
for _ in range(n+m):
	person = input()
	people[person] += 1
result = 0
result_list = []
for key, val in people.items():
	if val == 2:
		result += 1
		result_list.append(key)
print(str(result)+'\n')
for person in sorted(result_list):
	print(person)