num = int(input())
multiple = 1
cnt = 1
while (num > 1):
	num -= 6 * multiple
	multiple += 1
	cnt += 1
print(cnt)