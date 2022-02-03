 def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # 이득
        min_price = sys.maxsize
        
        for price in prices :
            min_price = min(price, min_price) # price값중 가장 작은 값으로 갱신
            profit = max(profit, price - min_price) # 이득의 최댓값을 profit으로 
        
        return profit
