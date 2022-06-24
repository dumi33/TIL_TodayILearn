from collections import deque
def solution(n, edge):
    vis =[ 0 for i in range(n+1)]
    #vis = [0]*(n+1)
    mp = [[] for i in range(n+1)]
    
    for a,b in edge :
        mp[a].append(b)
        mp[b].append(a)
    vis[1] =1
    q = deque([1])
    
    while q:
        cur = q.popleft()
        for new in mp[cur] :
            if vis[new] == 0:
                vis[new] = vis[cur] +1 
                q.append(new)
    max_v = max(vis)
    answer = vis.count(max_v)
    return answer
