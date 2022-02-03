import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V,E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
dis = [INF]*(V+1)

for _ in range(E) :
    u,v,w = map(int,input().split())
    graph[u].append([w,v])

heap = []

def Dijkstra(start):
    dis[start] = 0
    heapq.heappush(heap,(0,start))

    while heap :
        wei, node = heapq.heappop(heap)
        if dis[node] < wei : continue # 최단거리도 아닌거 볼필요가 없지

        for w, new_node in  graph[node] :
            new_w = w+wei 
            if dis[new_node] > new_w :
                dis[new_node] = new_w 
                heapq.heappush(heap,(new_w,new_node))


Dijkstra(K)

for i in range(1,V+1) :
    print("INF" if dis[i]==INF else dis[i])
