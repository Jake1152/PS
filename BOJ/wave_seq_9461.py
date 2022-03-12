memo = [0 for _ in range(101)]
for idx in range(4):
	memo[idx] = 1
	
def find_wave_seq(num):
	if num < 0:
		return 0
	if memo[num] != 0:
		return memo[num]
	memo[num] = find_wave_seq(num-2) + find_wave_seq(num-3)
	return memo[num]

t = int(input())
for _ in range(t):
	n = int(input())
	print(find_wave_seq(n))
