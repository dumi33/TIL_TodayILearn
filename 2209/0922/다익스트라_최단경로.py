def dijkstra(start) :
    #  시작점에서 시작점의 거리는 0
    distance[start] = 0 
    q = []
    
    # 거리는 0, 노드는 start
    heapq.heappush(q,[0,start])
    while q :
        dist, node = heapq.heappop(q)
        # 만약 dist가 현재 있는 거리보다 작으면 실행 X 
        if dist > distance[node] : continue
        
        # node에서 갈 수 있는 정점들을 돌면서 
        for i in mp[node] :
            cost = dist + i[1]
            # 새로운 거리가 원래 길이보다 작다면 
            if cost < distance[i[0]] :
            	# 갱신을 해주고 
                distance[i[0]] = cost 
                # heap에 넣는다.
                heapq.heappush(q,[cost,i[0]])
    
    
if __name__=="__main__" :
    V,E = map(int,input().split())
    k = int(input())
    
    mp = [[] for _ in range(V+1)]
    distance = [int(1e9)] * (V+1)


    for _ in range(E) :
        u,v,w = map(int,input().split())
        mp[u].append([v,w])
    
    dijkstra(k)
    
    for i in range(1,V+1) :
        print("INF" if distance[i] == int(1e9) else distance[i] )
