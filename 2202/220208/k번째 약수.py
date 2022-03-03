import sys
#sys.stdin = open("input.txt", "rt") 
divisor = []
n,k = map(int,input().split())
for i in range(1,n+1) :
    if n%i == 0 :
        divisor.append(i)
if len(divisor) >= k : print (divisor[k-1]) # 이 부분에서 좀 틀림 
else : print(-1)
