
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for i in range(bridge_length)] 
    while bridge : # 건널 트럭이 없어도 다리를 탄 트럭이 다리를 건너야하므로 
        answer+=1
        bridge.pop(0)
            
        if truck_weights :
            tmp = truck_weights[0]
            if tmp + sum(bridge) > weight :
                bridge.append(0)
            else :
                bridge.append(truck_weights.pop(0))
        
    return answer
