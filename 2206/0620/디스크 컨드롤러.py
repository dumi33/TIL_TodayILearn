import heapq
def solution(jobs):
    answer, start, now = 0, -1, 0
    i = 0
    heap = []
    while i < len(jobs) :
        for job in jobs :
            if start < job[0] <= now :
                heapq.heappush(heap,[job[1],job[0]])
        if heap :
            cur= heapq.heappop(heap)
            start = now 
            now += cur[0]
            i+=1
            answer+=now - cur[1]
        else :
            now+=1 
    return answer // len(jobs)
            
