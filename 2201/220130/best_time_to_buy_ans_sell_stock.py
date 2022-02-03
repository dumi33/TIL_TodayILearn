def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # 수익
        min_price = sys.maxsize
        for price in prices : 
            min_price = min(min_price, price) # 저점 찾기
            profit = max(price-min_price, profit)
        return profit
