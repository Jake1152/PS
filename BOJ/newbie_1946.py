from sys import stdin

t = int(stdin.readline())
result = []
for _ in range(t):
	n = int(stdin.readline())    
	cnt = 0
	applicants = [0 for _ in range(n)]
	#n번째까지 있는 것을 이미 알고 있으므로 input받을때 정렬된 순서대로 들어오게 만들수 있다.
	for _ in range(n):
		score ,interview = map(int, stdin.readline().split())
		applicants[score-1] = (score ,interview)
	
	# applicants, candidate 두개로 분류  candidate는 이미 통과
	min_inter = n+1
	for evalue in applicants:
		if min_inter > evalue[1]:
			cnt += 1
			min_inter = evalue[1]
	result.append(cnt)
	
for ele in result:
	print(ele)
