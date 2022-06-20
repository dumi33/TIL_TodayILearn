def solution(n, computers):
    answer = 0
    vis = [0 for i in range(n)]
    def dfs(now) :
        vis[now] = 1
        for new in range(n) :
            if computers[now][new] and vis[new] == 0 :
                dfs(new)
    
    for i in range(n) :
        if vis[i] == 0 :
            dfs(i)
            answer +=1 
            
    return answer
