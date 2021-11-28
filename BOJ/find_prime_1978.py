def check_prime(the_number):
	if the_number <= 1:
		return False
	for num in range(2, int(the_number**0.5)+1):
		if the_number % num == 0:
			return False
	return True

def remove_multi_num(num, to_be_prime_list, limit):
	for mul_num in range(num*2, limit+1, num):
		if mul_num in to_be_prime_list:
			to_be_prime_list.remove(mul_num)
	
def elatostenes(number):
	to_be_prime_list = [i for i in range(2, number+1)]
	for num in to_be_prime_list:
		if check_prime(num):
			remove_multi_num(num, to_be_prime_list, number)
	return (to_be_prime_list)

che = elatostenes(1000)
N = int(input())
cnt = 0

for num in map(int, input().split()):
	if num in che:
		cnt += 1
print(cnt)