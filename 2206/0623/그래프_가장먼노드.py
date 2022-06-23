from collections import deque
def solution(n, edge):
    vis = [0 for i in range(n+1)]
    mp = [[] for i in range(n+1)]
    
    for a,b in edge :
        mp[a].append(b)
        mp[b].append(a)
    
    q = deque()
    q.append(1)
    vis[1] = 1
    
    while q :
        cur = q.popleft()
        for i in mp[cur] :
            if vis[i] == 0:
                vis[i] = vis[cur] +1 
                q.append(i)
    
    max_v = max(vis)
    answer = vis.count(max_v)
    return answer
