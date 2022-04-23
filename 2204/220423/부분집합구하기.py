def dfs(L) :
    if  L == (x+1) : 
        for i in range(1,x+1) :
            if arr[i] == 1 :
                print(i,end='')
        print()
    else :
        arr[L] = 1; # L번째 숫자를 넣는경우
        dfs(L+1)
        arr[L] = 0; # L번째 숫자를 넣지않는 경우 
        dfs(L+1)
        
    
if __name__=="__main__" : 
    x = int(input())
    arr = [0]*(x+1) # 배열은 0부터 시작하므로 제대로 출력하려면 x+1까지 배열을 만들어야한다. 
    dfs(1)
