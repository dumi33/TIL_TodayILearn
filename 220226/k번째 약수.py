# 내가 만든 풀이
# 채점 결과 맞음 
if __name__ == "__main__" :
    cnt = 0
    n,k = map(int,input().split())
    for i in range(1,n+1) :
        if n %i == 0 : # i 가 약수
            cnt+=1
            if cnt == k :
                print(i)
                break
    else : 
        print(-1)
