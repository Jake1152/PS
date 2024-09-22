'''
1칸 또는 2칸을 한번에 갈 수 있다.
가장 높은 계단까지 방법의 중복 없이 오를 수 있는 경우는 몇 가지인가?
1단 -> 1칸
2단 -> 1 + 1, 2 2
3단 -> 1 + 1 + 1, 2 + 1, 1 + 2  3
       f(2) + 1, f(1) + 2
4단 -> 1 + 1 + 1 + 1, 1 + 1 + 2, 1 + 2 + 1, 2 + 1 + 1, 2 + 2
      f(3) + 1, f(2) + 2
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        stair_dp = [0 for _ in range(max(n + 1, 3))]
        stair_dp[1] = 1
        stair_dp[2] = 2

        for num in range(3, n + 1):
            stair_dp[num] = stair_dp[num-1] + stair_dp[num-2]

        return stair_dp[n]
