import sys
import heapq
V,E = map(int,input().split())
K = int(input())
INF = sys.maxsize
graph = [[] for _ in range(V+1)]
dis = [INF]*(V+1)

for i in range(E) :
    u,v,w = map(int,input().split())
    graph[u].append([w,v])

heap = []

def Dijkstra(start) :
    heapq.heappush(heap,(0,start))
    dis[start] = 0

    while heap :
        w,node = heapq.heappop(heap)
        if dis[node] < w : continue

        for wei, new_node in graph[node] :
            new_wei = w + wei
            if dis[new_node] > new_wei :
                dis[new_node] = new_wei 
                heapq.heappush(heap,(new_wei,new_node))

Dijkstra(K)

for i in range(1,V+1) :
    print("INF" if dis[i]==INF else dis[i])