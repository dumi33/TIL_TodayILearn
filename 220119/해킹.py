import sys
import heapq
input = sys.stdin.readline # 속도향상
INF = sys.maxsize # 최댓값 

tc = int(input()) # test case 입력
heap =[]

def Hacking(n,d,c) :
    global heap
    global INF
    graph = [[] for _ in range(n+1)] 
    dis = [INF] * (n+1)
    for _ in range(d) :
        u,v,w = map(int,input().split())
        graph[v].append([w,u]) # u가 v를 의존하므로 v가 걸리면 u가 전염
    
    heapq.heappush(heap,(0,c)) # 처음을 힙큐에 삽입
    dis[c]=0
    
    while heap :
        w,node = heapq.heappop(heap)
        for wei,new_node in graph[node] :
            new_wei = wei+w  
            if dis[new_node] > new_wei : # 원래 값보다 작으면 
                dis[new_node] = new_wei
                heapq.heappush(heap,(new_wei,new_node))
    cnt=0
    time = 0

    for i in range(1,n+1) :
        if dis[i]!= INF : # 감염 안된것들은 제외
            cnt+=1 # 감염된 개수 
            if dis[i] > time : time = dis[i] # 소요된 시간 
    print(cnt, time)

for _ in range(tc) :
    n,d,c = map(int,input().split())
    Hacking(n,d,c)
