import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
heap = []

def hacking(n,d,c):
    global INF
    global heap

    graph = [[] for _ in range(n+1)]
    dis = [INF] * (n+1)

    for _ in range(d) :
        u,v,w = map(int,input().split())
        graph[v].append([w,u]) # 의존성 관계를 잘 이해하고 넣기 
    
    heapq.heappush(heap,(0,c))
    dis[c] = 0
    while heap : # 전형적인 다익스트라
        w, node = heapq.heappop(heap)
        for wei , new_node in graph[node] :
            new_wei = wei + w
            if dis[new_node] > new_wei :
                dis[new_node] = new_wei
                heapq.heappush(heap,(new_wei, new_node))
    cnt = 0
    ans = 0
    for i in range(1,n+1) : # dis 배열을 돌면서
       if dis[i] != INF : 
           cnt+=1 # 감염된 컴퓨터의 수 count
           if ans < dis[i] : ans = dis[i] # 가장 오래걸리는 수를 ans에 기억
    print(cnt, ans)

case = int(input())
for _ in range(case) :
    n,d,c = map(int,input().split())
    hacking(n,d,c)
