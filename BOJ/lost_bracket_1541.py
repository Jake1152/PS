# lost bracket
from sys import stdin
input = stdin.readline
input_value = input().strip()
num = ''
# sign = []
num_list = []
for ch in input_value:
	if ch == '-' or ch == '+':
		if num != '':
			num_list.append(int(num))
			num = ''
		num_list.append(ch)
	else:
		num += ch
if num != '':
	num_list.append(int(num))
minus_flag = False
result = 0
for value in num_list:
	if value == '-':
		minus_flag = True
	elif value != '-' and value != '+':
		if minus_flag:
			result -= value
		else:
			result += value
print(result)


'''
음수가 나오면 기존 값에서 
새로운 음수가 나올때까지 무조건 뺸다.
'''