def dfs(L,P) :
    global cnt
    if L==n:
        cnt+=1
        for j in range(P) :
            print(chr(res[j]+64),end='') # 문자열으로 출력
        print()
    else :
       for i in range(1,27) : # 알파벳은 26까지 있음 
           if code[L] ==i  : # 한자리수 
               res[P]=i 
               dfs(L+1, P+1)
           elif i>=10 and code[L] == i//10 and code[L+1]==i%10 : # 두자리수 
               res[P] = i
               dfs(L+2, P+1)
    
            
if __name__=="__main__" :
    code = list(map(int,input())) # 각 숫자를 하나의 요소로 만듦
    n = len(code)
    code.insert(n,-1) # 2자리수를 비교할 때 outofrange가 발생하지 않도록 
    res = [0]*n
    cnt = 0
    dfs(0,0)
    print(cnt)
