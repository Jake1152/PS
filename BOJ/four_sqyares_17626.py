# Four Squares 17626


'''
- 0.5 Square
- 가장 근사값을 찾는다.
- 몇으로 줄면 더이상 계산할 필요가 없는가?
    - 모든 자연수는 구할수있다고 하였으니 안되는 경우는 생각할 필요가 없다.
- DP인 요소는 무엇인가?
    - 점화식은 어떻게 되는가?
    - 최대 4개
    - 
- square 
'''


def recur_square(org_num):
    if org_num == 0:
        return 0
    if  org_num < 0:
        return 
    root_n = int(org_num ** 0.5)
    diff = org_num - root_n ** 2
    print(f"{diff=}")
    return recur_square(diff) + 1

n = int(input())
print(f"{recur_square(n)=}")
# while (n):



n = int(input())
dp =  [0,1]
for i in range(2, n+1):
    min_value = 1e9
    j = 1
    while (j**2) <= i:
        min_value = min(min_value, dp[i - (j**2)])
        j += 1
    dp.append(min_value + 1)
print(dp[n])