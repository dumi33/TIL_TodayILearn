from collections import deque
def solution(prices):
    answer = []
    d = deque(prices)
    while d :
        tmp_ans = 0
        tmp = d.popleft()
        for price in d :
            tmp_ans +=1 
            if price < tmp :
                break
        answer.append(tmp_ans)
    return answer
