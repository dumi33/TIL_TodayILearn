import heapq
def solution(operations):
    answer = []
    heap = []
    for oper in operations :
        oper = oper.split()
        if oper[0]=="I" :
            heapq.heappush(heap, int(oper[1]))
        else :
            if len(heap)==0 :
                pass
            elif oper[1] == "1":
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
            else :
                heapq.heappop(heap)
    if len(heap) == 0 :
        answer.append(0)
        answer.append(0)
    else :
        answer.append(max(heap))
        answer.append(min(heap))
            
    return answer
