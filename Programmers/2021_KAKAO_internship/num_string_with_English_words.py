#num_string_with_English_words.py

def solution(s):
	answer = ""
	eng_words_dict = \
	{"zero"  : 0, "one"   : 1, "two"   : 2, "three" : 3, "four"  : 4,\
	"five"  : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine"  : 9}
	eng_word = ""
	for ch in s:
		if ch.isalpha() == True:
			eng_word +=  ch
			if eng_words_dict.get(eng_word):
				answer += str(eng_words_dict[eng_word])
				eng_word = ""
		else:
			if eng_words_dict.get(eng_word):
				answer += str(eng_words_dict[eng_word])
			answer += ch
			eng_word = ""
	if eng_word:
		answer += eng_words_dict[eng_word]

	return int(answer)


s = "one4seveneight"
print(solution(s))

'''
"one4seveneight"	1478


'''