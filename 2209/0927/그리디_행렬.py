def flip(i,j) :
    for x in range(i,i+3) :
        for y in range(j,j+3) :
            if original[x][y] == 0 :
                original[x][y] = 1 
            else : original[x][y] = 0

        
if __name__=="__main__" :
    n,m = map(int,input().split())
    
    original =[list(map(int,list(input()))) for _ in range(n)]
    goal =[list(map(int,list(input()))) for _ in range(n)]

    cnt = 0
     
    for i in range(n-2) :
        for j in range(m-2) :
            if original[i][j] != goal[i][j] :
                flip(i,j)
                cnt+=1 

    print(-1 if original != goal else cnt)
