import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]


for _ in range(E) :
    a,b,c = map(int ,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

v1,v2 = map(int,input().split())

heap = []
def Dijkstra(start) :
    dis = [INF]*(N+1)
    dis[start] = 0
    heapq.heappush(heap,(0,start))

    while heap :
        w,node = heapq.heappop(heap)
        if dis[node] < w : continue
        for c,v in graph[node] :
            if dis[v] > c+w :
                dis[v] = c+w
                heapq.heappush(heap,(c+w,v))
    return dis

load1 = Dijkstra(1) # 1에서 시작하는 최단거리
loadv1 = Dijkstra(v1) # v1에서 시작하는 최단거리
loadv2 = Dijkstra(v2)# v2에서 시작하는 최단거리

path1 = load1[v1] + loadv1[v2]+loadv2[N]
path2 = load1[v2] + loadv2[v1]+loadv1[N]

path = min(path1,path2)

print(path if path<INF else -1)
