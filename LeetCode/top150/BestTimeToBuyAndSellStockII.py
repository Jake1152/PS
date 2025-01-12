class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        - 
        '''
        result = 0
        for idx in range(len(prices)):
            stock = prices[idx]
            cur_sum = 0
            for price in prices[idx+1:]:
                if price > stock:
                    cur_sum += price - stock
                    stock = price
            result = max(result, cur_sum)
        return result
