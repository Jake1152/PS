# set 11723 

from sys import stdin

input = stdin.readline
cmd_cnt = int(input())
s = set()
for _ in range(cmd_cnt):
	cmd_list = input().strip().split()
	if cmd_list[0] == "all":
		s = set([i for i in range(1,21)])
		continue
	if cmd_list[0] == "empty":
		s = set()
		continue
	cmd, num = cmd_list[0], int(cmd_list[1])
	if cmd == "add":
		s.add(num)
	elif cmd == "check":
		if num in s:
			print(1)
		else:
			print(0)
	elif cmd == "remove" and (num in s):
		s.remove(num)
	elif cmd == "toggle":
		if num in s:
			s.remove(num)
		else:
			 s.add(num)