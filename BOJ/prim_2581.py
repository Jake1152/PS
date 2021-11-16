start_num = int(input())
end_num = int(input())
min_prim = end_num
sum_prim = -1
def check_prime(num):
	if num <= 1:
		return False
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return False
	return True

for num in range(start_num, end_num+1):
	if check_prime(num):
		sum_prim += num
		if min_prim > num:
			min_prim = num
if sum_prim == -1:
    print(sum_prim)
else:
    print(sum_prim)
    print(min_prim)
	


