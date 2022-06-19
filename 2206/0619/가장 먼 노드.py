from collections import deque
def solution(n, edge):
    mp =[[]for i in range(n+1)]
    vis = [0] * (n+1)
    
    for a,b in edge :
        mp[a].append(b)
        mp[b].append(a)
    
    vis[1] = 1
    q = deque([1])
    
    while q :
        now = q.popleft()
        for i in mp[now] :
            if vis[i] == 0 :
                vis[i] = vis[now]+1 
                q.append(i)
                
    max_v = max(vis)
    answer = vis.count(max_v)
        
    return answer
