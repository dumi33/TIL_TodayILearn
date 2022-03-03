def dfs(x) :
    if x == n+1 :
        for i in range(len(ch)) :
            if ch[i] == 1 :
                print(i, end = ' ')
        print()
    else :
        ch[x] =1 
        dfs(x+1)
        ch[x] =0 
        dfs(x+1)


if __name__ == "__main__" :
    n = int(input())
    ch = [0]*(n+1) # 0부터 n까지
    dfs(1)
