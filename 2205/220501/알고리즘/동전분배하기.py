def dfs(L) :
    global ans 
    if L == n :
        cha = max(money) - min(money)
        if cha < ans :
            s = set() # 서로 분배된 돈이 달라야하므로
            for j in money :
                s.add(j)
            if len(s) == 3 : ans =  cha
    else :
        for i in range(3) :
            money[i]+=arr[L]
            dfs(L+1)
            money[i]-=arr[L]
    
if __name__=="__main__" :
    money = [0]*3
    n = int(input())
    arr = []
    for i in range(n) :
        tmp = int(input())
        arr.append(tmp)
    ans = sys.maxsize
    dfs(0)    
    print( ans )
