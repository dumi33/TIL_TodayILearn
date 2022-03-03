def dfs(x) :
    global cnt
    if x == n : 
        cnt += 1
    else :
        for i in range(1,n+1) :
            if arr[x][i] == 1 and ch[i] == 0:
                ch[i] = 1
                dfs(i)
                ch[i] = 0

if __name__ == "__main__" :
    n,m =map(int,input().split())
    arr = list([0]*(n+1) for i in range(n+1))
    for i in range(m) :
        x,y = map(int,input().split())
        arr[x][y] = 1
    cnt = 0
    ch = [0]*(n+1)
    ch[1] = 1
    dfs(1)
    print(cnt)
