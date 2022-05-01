from collections import deque
if __name__=="__main__" :
    s,e = map(int,input().split())
    dq = deque()
    MAX = 10000
    arr = [0]*(MAX+1)
    ch= [0]*(MAX+1)
    
    dq.append(s)
    ch[s] = 1
    while dq : # 덱에 무언가 있는 동안 
        now = dq.popleft()
        for next in (now+1, now-1, now+5) :
            if 0<next <= MAX and ch[next]==0 : #  구간안에 존재하고, 가보지않았다면 
                ch[next] = 1 
                dq.append(next)
                arr[next] = arr[now] +1 
    print(arr[e])
