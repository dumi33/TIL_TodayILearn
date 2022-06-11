def solution(progresses, speeds):
    answer = []
    cnt = 0
    time = 0
    while progresses :
        if (progresses[0] +speeds[0]*time >=100) : # 하나 기능 개발 완료 
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1 
        else : # 시간이 더 필요 
            if cnt > 0 : # 연속으로 개발을 할수있었는데...
                answer.append(cnt)
                cnt = 0 
            time +=1 
    answer.append(cnt)
    return answer
