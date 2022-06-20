import heapq 
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville : 
        if scoville[0] >= K :
            return answer 
        if len(scoville) ==1 :
            return -1 
        answer +=1 
        Min1 = heapq.heappop(scoville)
        Min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, Min1 + (Min2*2))
