import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V,E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
dis = [INF]*(V+1)

heap = []
for _ in range(E) :
    u,v,w = map(int,input().split())
    graph[u].append([w,v])

def Dijkstra(start) :
    dis[start] = 0
    heapq.heappush(heap,(0,start))
    
    while heap :
        w,node = heapq.heappop(heap)
        if dis[node] < w : continue

        for wei, new_node in graph[node] :
            new_wei = wei + w 
            if dis[new_node] >  new_wei :
                dis[new_node] =  new_wei 
                heapq.heappush(heap,(new_wei,new_node))

Dijkstra(K)

for i in range(1,V+1) :
    print("INF" if dis[i]==INF else dis[i])