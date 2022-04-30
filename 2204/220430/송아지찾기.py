from collections import deque
if __name__=="__main__" :
    s,e = map(int,input().split())
    MAX = 10000
    ch = [0]*(MAX+1)
    dis = [0]*(MAX+1)
    ch[s] = 1
    dis[s] = 0
    dq = deque()
    dq.append(s)
    while dq :
        now = dq.popleft()
        for next in (now+1,now+5,now-1) :
            if 0<next<=MAX and ch[next] ==0  :
                dq.append(next)
                ch[next] = 1
                dis[next] = dis[now]+1
    print(dis[e])
