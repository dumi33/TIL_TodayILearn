def solution(routes):
    answer = 0
    routes.sort(key = lambda x :x[1])
    
    camera = -30001
    for i in routes :
        if camera < i[0] :
            camera = i[1]
            answer += 1
        else :
            continue
    
    return answer
