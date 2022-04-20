def dfs(v) :
    if v == n+1 :
        for i in range(1,n+1) : # 1부터 사용
            if ch[i] == 1 :  # 1인 상태의 숫자만 출력
                print(i,end=' ')
        print()
    else :
        ch[v] = 1
        dfs(v+1)
        ch[v] = 0
        dfs(v+1)
        
if __name__=="__main__" : 
    n = int(input())
    ch = [0]*(n+1)
    dfs(1)
