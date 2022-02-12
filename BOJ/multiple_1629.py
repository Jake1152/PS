def power_recursion(base, power, mode_num):
	if (power == 1):
		return base % mode_num
	else:
		tmp = power_recursion(base, power // 2, mode_num)
		if power % 2 == 0:
			return tmp * tmp % mode_num
		else:
			return tmp * tmp * base % mode_num

num, power, mode_num = map(int, input().split())
print(power_recursion(num, power, mode_num))


'''
2 * 
16
4 4
2 2 2 2

import sys
sys.setrecursionlimit(2*31)
num, power, mode_num = map(int, input().split())

def power_recursion(num, power, mode_num):
	if (power == 1):
		return num
	mul = power_recursion(num, power//2, mode_num)
	if (power % 2 != 0):
		return (mul % mode_num) * (mul % mode_num)
	else:
		return (mul % mode_num) * (mul % mode_num) * (num % mode_num) % mode_num
	return mul

print(power_recursion(num, power, mode_num))


'''