from collections import deque
def solution(prices):
    answer = []
    d = deque(prices)
    while d :
        tmp = d.popleft() # deque에 있는 함수 
        tmp_ans = 0 
        for i in d : # 남은 d에 있는 값들을 빼와서 비교 
            tmp_ans+=1 
            if tmp > i : 
                break 
        answer.append(tmp_ans)
    return answer
