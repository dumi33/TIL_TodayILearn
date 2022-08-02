from collections import deque
from itertools import combinations as c 


dx = [1,0,-1,0]
dy = [0,1,0,-1]

if __name__=="__main__" :
    n = int(input())
    dic = {}
    mp = [[0]*n for i in range(n)]
    
    for i in range(n**2) :
        a,b,c,d,e = map(int,input().split())
        dic[a] = [b,c,d,e]
    
    for k in dic.keys() :
        tmp =[]
        for i in range(n) :
            for j in range(n) :
                if mp[i][j] == 0 :
                    friend, empty = 0,0
                    for idx in range(4) :
                        nx,ny = i + dx[idx] , j + dy[idx]
                        if 0<=nx<n and 0<=ny<n :
                            if mp[nx][ny] in dic[k] :
                                friend +=1 
                            elif mp[nx][ny] == 0 :
                                empty +=1 
                    tmp.append([friend, empty, i,j])
        tmp.sort(key = lambda x : (-x[0],-x[1],x[2],x[3]))  
        mp[tmp[0][2]][tmp[0][3]] = k 
    ans =0
    for i in range(n) :
        for j in range(n) :
            cnt = 0
            for dir in range(4) :
                nx,ny = i + dx[dir], j + dy[dir]
                if 0<=nx<n and 0<=ny<n and mp[nx][ny] in dic[mp[i][j]] :
                    cnt +=1 
            if cnt > 0 :
                ans += 10**(cnt-1)
    print(ans) 
