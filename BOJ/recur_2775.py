# 2775
dp = [[ 0 for _ in range(14+1) ] for _ in range(14+1)]
for i in range(1, 14+1):
	dp[0][i] = i

def recursion(layer, room):
	# print(f"{dp[layer][room]=}")
	if dp[layer][room] != 0:
		return dp[layer][room]
	for sublayer_room in range(1, room+1):
		dp[layer][room] += recursion(layer-1, sublayer_room)
	return dp[layer][room]

t = int(input())
for _ in range(t):
	k = int(input())
	n = int(input())
	print(recursion(k, n))

'''
a a a
1 2 3 


'''