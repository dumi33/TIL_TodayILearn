if __name__=="__main__" :
    n,m = map(int,input().split())
    dy = [0]*(m+1)
    for i in range(n) : # 보석을 돌면서 
        w,v = map(int,input().split())
        for j in range(w,m+1) :
            # 원래 값과 보석을 넣은 값중 큰값으로 갱신 
            dy[j] = max(dy[j], dy[j-w]+v)
    print(dy[m])
