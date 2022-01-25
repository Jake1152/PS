#tall building 1027
N = int(input())
buildings = list(map(int, input().split()))
B = [0] * N

# 기울기 만족해야한다.
for i in range(N):
	e = -99999999999
	for j in range(i+1, N):
		d = (buildings[j] - buildings[i]) / (j - i)
		if d > e:
			e = d
			B[i] += 1
			B[j] += 1
res = 0
for i in B:
	res = max(res, i)
print(res)


'''
N = int(input())
buildings = list(map(int, input().split()))
max_views = 0
idx = -1

while (idx < N):
	view = 0
	idx_flag = False
	# left bound
	prev_idx = idx-1
	print(f"{buildings[idx]=}")
	for left_idx in range(idx-1,-1,-1):
		view += 1
		if buildings[idx] <= buildings[left_idx] or buildings[left_idx] <= buildings[prev_idx]:
			break
		prev_idx = left_idx
	# right bound
	prev_idx = idx
	for right_idx in range(idx, len(buildings)):
		view += 1
		if buildings[right_idx] <= buildings[prev_idx]:
			idx_flag = True
			break
		prev_idx = right_idx
	if (view > max_views):
		max_views = view
	if (idx != N-1 and idx_flag):
		idx = right_idx
	else:
		idx += 1
print(max_views)
'''

'''
# 문제이해
볼수있는 빌딩이 가장 많은 빌딩에서 봤을 때 보이는 빌딩의 개수는 몇개인가?

# 문제 재정의
중간에 시야 가리는것 없이
볼수있는 빌딩의 개수가 최대가 될떄 몇개인가?
양뱡향으로 볼 수 있다.

# 문제해결방법
처음부터 시작 
현재 위치에서 좌,우 양방향으로 보면서 볼 수 있는 건물의 갯수를 세고서 
max_views와 비교해서 max_views보다 더 크면 갱신한다.

- 다음 index는 현재 빌딩보다 큰 높이의 빌딩으로한다
- 좌, 우로 순회한다.
	기준은 나보다 작아야하고 
	선분이 되는 끝점이 빌딩은 이전 빌딩보다 점점 커져야한다.
	그러다가 끝점에 빌딩이 현재 기준이 되는 빌딩의 높이와 같거나 더 커지면
	순회를 멈춘다.(왼쪽의 경우.)
	
	오른쪽의 경우 순회를 멈춘 뒤에 다음 기준 빌딩을 그 크던 빌딩 혹은 같은 높이의 빌딩으로 바꾼다.


# 검증


# 실행


# 회고



'''