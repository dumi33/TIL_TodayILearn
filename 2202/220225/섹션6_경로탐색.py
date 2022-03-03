def dfs(x) :
    global cnt
    if x==n: # 5번 노드로 도착
        cnt += 1
    else :
        for i in range(1,n+1) :
            if graph[x][i] == 1 and ch[i]==0 : # 길이 있고 가지 않았다면 
                ch[i] = 1 # 갔음을 표시 
                dfs(i)
                ch[i] = 0

if __name__ == "__main__" :
    
    n,m = map(int,input().split())
    ch = [0] * (n+1)
    cnt = 0 #  경우의 수 
    graph = [[0]*(n+1) for i in range(n+1)]
    for _ in range(m) :
        a,b = map(int,input().split())
        graph[a][b] = 1  # a에서 b를 갈 수 있다. # 이차원 배열 이란다
    ch[1] = 1  # 잊어버리지 말기 
    dfs(1) # 1에서 시작하여 n으로가는 경우의 수를 구한다.
    print(cnt)
    
