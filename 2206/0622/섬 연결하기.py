def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    connect = set([costs[0][0]])
    
    while len(connect) < n :
        for cur in costs :
            if cur[0] in connect and cur[1] in connect :
                continue
            elif cur[0] in connect or cur[1] in connect :
                answer += cur[2]
                #connect.update([cur[0],cur[1]])
                connect.add(cur[0])
                connect.add(cur[1])
                break

    return answer
