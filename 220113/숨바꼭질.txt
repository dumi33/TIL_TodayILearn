from collections import deque
queue = deque()
n,k = map(int, input().split())

arr = [-1]*100001

def bfs(n) :
    queue.append(n)
    while queue : 
        node = queue.popleft()
        for i in (node+1, node-1, node*2) : # 이 부분을 range(node+1,node-1,...)으로 했어서 틀렸었다. 
            if 0<=i<=100000 and arr[i]==-1 : 
                arr[i] = arr[node]+1
                queue.append(i)
arr[n] =0
bfs(n)
print(arr[k])