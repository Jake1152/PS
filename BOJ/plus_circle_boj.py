num = str(input())
org = [num]
cnt = 0

while (True):
	sum = 0
	for digit in list(num):
		sum += int(digit)
	num = str(num[-1]) + str(sum)[-1]
	cnt += 1
	if int(org[0]) == int(num):
		break
print(cnt)