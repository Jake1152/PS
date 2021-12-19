from collections import Counter
word = input().upper()
prev_cnt = 0
most_common_alpha = Counter(list(word)).most_common(2)
for alpha, cnt in (most_common_alpha):
    if prev_cnt == cnt:
        print("?")
        break
    else:
        prev_cnt = cnt
else:
    print(most_common_alpha[0][0])
