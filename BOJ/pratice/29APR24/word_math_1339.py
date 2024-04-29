from collections import defaultdict

alpha_weight = defaultdict(int)

word_count = int(input())
for _ in range(word_count):
    word = input()
    word_length = len(word)
    for idx, char in enumerate(word):
        exponent = word_length - (idx + 1)
        weight = 10 ** exponent
        alpha_weight[char] += weight

result = 0
for idx, (_, weight) in enumerate(sorted(alpha_weight.items(), key=lambda x: x[1],reverse=True)):
    num = 9 - idx
    result += weight * num 

print(result)

        
