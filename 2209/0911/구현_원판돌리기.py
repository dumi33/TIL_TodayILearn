from collections import deque

if __name__=="__main__" :
    n,m,t = map(int,input().split())
    mp = []
    for i in range(n) :
        mp.append(deque(list(map(int,input().split()))))
        
    for _ in range(t) :
        x,d,k = map(int,input().split())
        result = 0 
        # 방향 회전 
        for i in range(n) :
            result += sum(mp[i])
            if (i+1)%x ==0  :
                if d == 0 :
                    mp[i].rotate(k)
                else:
                    mp[i].rotate(-k)
        if result >0 :
            delete = set()
            for i in range(n) :
                for j in range(m-1) :
                    if mp[i][j]!=0 and mp[i][j] == mp[i][j+1]: 
                        delete.add((i,j))
                        delete.add((i,j+1))
                if mp[i][0] !=0 and mp[i][0] == mp[i][-1] :
                    delete.add((i,0))
                    delete.add((i,m-1))
            for j in range(m) :
                for i in range(n-1) :
                    if mp[i][j] != 0 and mp[i][j] == mp[i+1][j] :
                        delete.add((i,j))
                        delete.add((i+1,j))
            
            if len(delete) >0 :
                for x,y in delete :
                    mp[x][y] = 0
            else :
                zero_cnt = 0
                max_v = 0
                for i in range(n) :
                    for j in range(m) :
                        if mp[i][j] == 0 : zero_cnt +=1 
                        else : max_v += mp[i][j]
                avg_v = max_v / ((m*n)-zero_cnt)
                
                for i in range(n) :
                    for j in range(m) :
                        if mp[i][j] != 0 and mp[i][j] > avg_v : mp[i][j] -=1 
                        elif mp[i][j] != 0 and mp[i][j] < avg_v : mp[i][j] +=1 
        else : 
            print(0)
            exit(0)
    ans = 0 
    for i in range(n) :
        ans += sum(mp[i])
    print(ans) 
