class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        yesterday_price = prices[0]
        for idx, today_price in enumerate(prices):
            if today_price > yesterday_price:
                profit = today_price - yesterday_price
                sum +=  profit
            yesterday_price = today_price
        return sum          

'''
언제 팔고, 언제 사는 것이 나을 것인가?
오늘이 어제보다 비싸면 팔고
싸면 산다. 
'''
