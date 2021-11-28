_ = input()
score_list = list(map(int, input().split()))
new_score_list = []
max_score = max(score_list)
for score in score_list:
    new_score_list.append((score/max_score) * 100)

print(sum(new_score_list) / len(new_score_list))
