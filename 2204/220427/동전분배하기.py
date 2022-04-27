def dfs(L) :
    global ans
    if L == n :
        tmp_ans=max(money) - min(money) 
        if tmp_ans < ans :
            tmp = set() # 세 사람의 총액은 서로 달랴야 하므로 
            for x in money :
                tmp.add(x)
            if len(tmp) == 3 :
                ans = tmp_ans
    else :
        for i in range(3) :
            money[i] += arr[L]
            dfs(L+1)
            money[i] -= arr[L]
            
if __name__=="__main__" :
    n = int(input())
    arr = []
    for i in range(n) :
        arr.append(int(input()))
    ans = sys.maxsize
    money = [0]*3 # 배열을 새로 만들어 값을 저장한다. 
    dfs(0)
    print(ans)
