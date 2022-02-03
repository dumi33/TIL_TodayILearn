import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N,E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E) :
    a,b,c = map(int,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

v1, v2 = map(int,input().split())

heap = []
def Dijkstra(start) : # start에서 시작하는 최단거리
    dis = [INF] * (N+1)
    dis[start] = 0
    heapq.heappush(heap,(0,start))
    while heap : 
        w, node = heapq.heappop(heap)
        for wei, new_node in graph[node] : 
            if dis[new_node] > wei + w :
                dis[new_node] = wei + w
                heapq.heappush(heap,(dis[new_node],new_node))

    return dis

dis1 = Dijkstra(1)
disv1 = Dijkstra(v1)
disv2 = Dijkstra(v2)

route1 = dis1[v1] + disv1[v2] + disv2[N]
route2 = dis1[v2] + disv2[v1] + disv1[N]

ans = min(route2, route1)
print(-1 if ans>=INF else ans )
