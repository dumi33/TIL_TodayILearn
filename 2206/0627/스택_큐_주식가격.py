from collections import deque 
def solution(prices):
    answer = []
    q = deque(prices)
    while q :
        val = q.popleft()
        cnt = 0
        for j in q :
            cnt+=1 
            if val > j :
                break
        answer.append(cnt)
    return answer
