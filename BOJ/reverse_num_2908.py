a_num, b_num = input().split()
if (a_num[::-1] > b_num[::-1]):
	print(a_num[::-1])
else:
	print(b_num[::-1])