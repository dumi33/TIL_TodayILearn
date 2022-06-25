def solution(n, computers):
    answer  = 0
    vis = [0 for i in range(n)]
    
    def dfs(x) :
        vis[x] = 1
        for i, val in enumerate(computers[x]) :
            if val and vis[i] == 0 :
                dfs(i)
        
    for i in range(n) :
        if vis[i] == 0 :
            dfs(i)
            answer += 1
    return answer
