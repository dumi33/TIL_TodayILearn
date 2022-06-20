def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for i in range(bridge_length)]
    
    while bridge :
        bridge.pop(0)
        answer +=1 
        if truck_weights :
            if (truck_weights[0] + sum(bridge)) <= weight :
                bridge.append(truck_weights.pop(0))
            else :
                bridge.append(0)
    return answer
