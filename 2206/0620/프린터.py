from collections import deque

def solution(priorities, location):
    answer = 0
    d = deque([v,i] for i,v in enumerate(priorities)) 
    while d :
        tmp = d.popleft()
        if len(d) == 0 :
            answer +=1
            return answer 
        if d and tmp[0] >= max(d)[0] :
            answer +=1 
            if tmp[1] == location :
                return answer
        else :
            d.append(tmp)
    
    return answer
