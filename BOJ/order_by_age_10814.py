from sys import stdin

input = stdin.readline
n = int(input())
members = []
for index in range(n):
	age, name = input().split()
	members.append((index, (int(age), name)))
for _, member_info in sorted(members, key=lambda x: (x[1][0], x[0])):
	age, name = member_info
	print(' '.join([str(age), name]))


	