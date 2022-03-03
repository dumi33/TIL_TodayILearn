import sys
#sys.stdin = open("input.txt", "rt") 
cnt = 0
n, k = map(int,input().split())
for i in range(1,n+1) :
    if n%i == 0 :
        cnt += 1
    if cnt == k :
        print(i)
        break
else : print(-1)
