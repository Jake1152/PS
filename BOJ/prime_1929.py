from sys import stdout

def check_prime(num):
	if num <= 1:
		return False
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return False
	return True

start_num, end_num = map(int, input().split())

for num in range(start_num, end_num+1):
	if check_prime(num):
		print(str(num)+'\n')
	

'''

# way2 eratosthenes sieve fail
print = stdout.write

start, end = map(int, input().split())
num_set = set(range(2, end+1))
for num in range(2, end+1):
	if num in num_set:
		num_set -= set(range(num+num,end+1,num))
for num in num_set:
	if num >= start:
		print(str(num)+'\n')

'''



'''
start, end = map(int, input().split())
num_set = (i for i in range(2,end+1))
for num in num_set:
	num_set - (i for i in range(num+num,end+1,num))
for num in num_set:
	if num >= start:
		print(num)
'''