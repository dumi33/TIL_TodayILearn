def dfs(L,P) :
    global ans 
    if L == n:
        ans += 1
        for j in range(P) :
            print(chr(res[j]+64),end='')
        print()
    else :
        for i in range(1,27) :
            if i == code[L] :
                res[P] = i
                dfs(L+1, P+1)
            elif i >=10 and i//10 == code[L] and i%10 == code[L+1]:
                res[P] = i
                dfs(L+2, P+1)
    
if __name__=="__main__" :
    code = list(map(int,input()))
    n = len(code)
    res = [0]*(n+1) # 각 경우의 알파벳을 담을 배열 
    ans = 0 # 알파벳이 만들어지는 경우의 수 
    code.insert(n,-1) # res으로 헷갈려서 틀림 
    dfs(0,0)
    print(ans)
