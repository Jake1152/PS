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

# print(f"{alpha_weight=}")
sorted_alpha_weight = sorted(alpha_weight.items(), key=lambda x: x[1],reverse=True) #(x[1], x[0])
# sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
# print(f"{sorted_alpha_weight=}")

result = 0
for idx, (alpha, weight) in enumerate(sorted_alpha_weight):
    #  alpha, weight = val
    num = 9 - idx
    # print(f"{idx=}, {weight=}")
    result += weight * num 

print(result)

        
