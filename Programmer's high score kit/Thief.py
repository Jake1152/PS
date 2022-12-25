def solution(money):
    house_cnt = len(money)
    odd_dp = [ 0 for _ in range(house_cnt) ]
    even_dp = [ 0 for _ in range(house_cnt) ]
    
    last_idx = house_cnt - 1
    odd_dp[0] = money[1]
    prev_idx = 1
    for idx, _ in enumerate(money):
        if odd_dp[idx] == 0 and prev_idx + 1 < idx and idx != last_idx:
            odd_dp[idx] = odd_dp[prev_idx]
            if money[idx] > money[idx + 1]:
                prev_idx = idx
                odd_dp[idx] += money[idx]
            elif (idx + 1) != last_idx:
                prev_idx = idx + 1
                odd_dp[idx] += money[idx + 1]

    even_dp[0] = money[0]
    prev_idx = 0
    for idx, _ in enumerate(money):
        if even_dp[idx] == 0 and prev_idx + 1 < idx and idx != last_idx:
            even_dp[idx] = even_dp[prev_idx]
            if money[idx] > money[idx + 1]:
                prev_idx = idx
                even_dp[idx] += money[idx]
            elif (idx + 1) != last_idx:
                prev_idx = idx + 1
                even_dp[idx] += money[idx + 1]
    answer = max(max(even_dp), max(odd_dp))
    return answer


a_money = [1, 2, 3, 1]
print(f"{solution(a_money)=}")