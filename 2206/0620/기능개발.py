def solution(progresses, speeds):
    answer = []
    cnt = 0
    time = 0
    while progresses :
        if (progresses[0] + (speeds[0]*time) >= 100 ):
            cnt+=1
            progresses.pop(0)
            speeds.pop(0)
        else :
            if cnt > 0 :
                answer.append(cnt)
                cnt = 0
            else :
                time +=1 
    answer.append(cnt)
    return answer
