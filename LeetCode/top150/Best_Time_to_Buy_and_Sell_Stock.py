'''
더 작은 날 구매한다
더 비싸진 날 판매한다 

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        buy_price = prices[0] # 더 작아지면 구매한다
        sell_price = prices[0] # 지금보다 비싸지면 판다
        profit = 0 # buy_price보다 비싸지면 팔았다고 가정한다.
        for price in prices[1:]:
            if (buy_price < price and price - buy_price > profit):
                profit = price - buy_price
            elif (buy_price > price):
                buy_price = price
        return profit
