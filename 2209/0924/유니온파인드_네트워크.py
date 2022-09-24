def union(parent,a,b) :
    a = find(parent,a)
    b = find(parent,b)
    if a< b : parent[b] = a 
    elif a >b : parent[a] = b 

def find(parent,x) :
    if x != parent[x] : parent[x] = find(parent,parent[x])
    return parent[x]

def solution(n, computers):
    parent = [0]*(n+1)

    
    for i in range(1,n+1) :
        parent[i] = i
    
    for i in range(n) :
        for j in range(n) :
            if computers[i][j] and i!=j : union(parent,i+1,j+1)
        
    maps = {}
    for idx in range(1,len(parent)) :
        v = find(parent, idx)
        if not v in maps: maps[v] = 1
        
    return len(maps)
