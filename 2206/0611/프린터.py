from collections import deque

def solution(priorities, location):
    answer = 0
    d = deque([(v,i) for i, v in enumerate(priorities)])
    while d : 
        tmp = d.popleft()
        if d and max(d)[0] > tmp[0] : # 나보다 우선순위가 높은 수가 있다면 
            d.append(tmp) # 다시 뒤에 붙인다. 
        else : # 출력 
            answer+=1 
            if (location == tmp[1]) :
                return answer
