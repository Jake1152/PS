class Solution:
    def rob(self, nums: List[int]) -> int:
        # 현재까지의 최대 합이 최대가 되어야함
        # 연속해서 가져올 수는 없음

        # case1 ㅁㅇㅁ
        # case2 ㅁㅇㅇㅁ
        # case3 ㅇㅁ
        '''
        마지막부터 시작
        현재 것을 선택하면 이전 것은 선택하지 못함
        현재 것을 선택하는 것과
        현재 기준 2개 전까지 중 가장 큰 것을 선택
        바로 직전 것은 선택할 수 없음 
        '''
        dp = [0] + [0 for _ in range(nums)]
        dp2 = [0] + [0 for _ in range(nums)]

        # 지금아니면 직전 것만 선택
        # 직전 것이 선택되었다면 제외해야함, 직전 것이 선택되었는지 여부는 전전것보다 값이 크면 선택된 것.

        # for idx in range(len(nums)-1, -1, -1):
        #     dp[idx] = max(dp[idx], )
        dp2
        house_len = len(nums)
        for idx, val in enumerate(nums):
            dp[idx+2]
        '''
        첫번째가 선택
        '''



        
