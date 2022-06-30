from collections import deque 
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices :
        cur = prices.popleft()
        time = 0
        for i in prices:
            time +=1 
            if i < cur :
                break
        answer.append(time)
    return answer
