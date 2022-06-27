from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([[v,i] for i,v in enumerate(priorities)])
    while q :
        cur  = q.popleft()
        if not q : return answer+1 
        if q and max(q)[0] <= cur[0] :
            answer+=1 
            if location == cur[1] : return answer
        else :
            q.append(cur)
