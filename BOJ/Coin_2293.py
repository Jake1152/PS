# coin_2293


# first way using recursion
# from collections import defaultdict

coins_species, target_amount = map(int, input().split())
coins = []
memo = [-1 for _ in range(target_amount+1)]
memo[0] = 1
for _ in range(coins_species):
    coins.append(int(input()))
coins.sort(reverse=True)
def recursion_coin_value(amount, coin_idx):
    print(f"{amount=}, {coin_idx=}")
    if amount < 0 or coin_idx >= coins_species:
        return 0
    elif memo[amount] != -1:
        print(memo[amount])
        return memo[amount]
    else:
        memo[amount] = recursion_coin_value(amount - coins[coin_idx], coin_idx) + recursion_coin_value(amount, coin_idx + 1)
        return memo[amount]

recursion_coin_value(target_amount, 0)
print(memo[target_amount])



'''
# second way bottom-up
coins_species, target_amount = map(int, input().split())
coins = []
dp = [0 for _ in range(target_amount+1)]
for _ in range(coins_species):
    coins.append(int(input()))
coins.sort()
for i in range(target_amount+1):
    for coin in coins:
        if i+coin <= target_amount:
            dp[i+coin] += 1
print(dp)
print(dp[target_amount])
'''