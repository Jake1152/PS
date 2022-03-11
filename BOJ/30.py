# import sys
# input = sys.stdin.readline
# print = sys.stdout.write
n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
	sum += int(i)
if sum % 3 != 0 or "0" not in n:
	print(-1)
else:
	print("".join(n))
# num_list = list(input().strip())
# if not '0' in num_list:	
# 	print('-1')
# else:	
# 	num_list.remove('0')
# 	num_list.sort(reverse=True)
# 	# print(f"{num_list=}\n")
# 	sum = 0
# 	for num in num_list:
# 		sum += int(num)
# 		if sum % 3 !=0:
# 			print("-1")
# 			break
# 	else:
# 		print(str(sum * 10))

	
'''
n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
	sum += int(i)
if sum % 3 != 0 or "0" not in n:
	print(-1)
else:
	print("".join(n))
'''
#
# 8 6 5 5 5 4 3 2 2 1 1 0