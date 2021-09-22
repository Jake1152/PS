def solution(n, words):
	answer = [0,0]    
	ltemp = []
	for idx, val in enumerate(words):        
		if idx > 0:
			if ((words[idx-1][-1] != val[0]) or 
				(val in ltemp)):
				if (idx+1)%n == 0:
					answer[0] = n
				else:
					answer[0] = (idx+1)%n
				answer[1] = (idx)//n+1
				return answer
		ltemp.append(val)
	return answer

'''
- 끝말잇기 규칙에 맞게 진행되는지
	마지막단어를 추출
- 각 단어가 중복인지
- 중복이거나 규칙에 안맞으면 몇번째 턴에, 어떤 참가자가 걸렸는지 결과값으로 return
	그렇지 않으면(중복도 없으며 규칙에도 맞으면)
	0,0을 리턴
'''