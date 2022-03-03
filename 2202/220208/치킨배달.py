
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int,input().split())
graph = []
for i in range(n) :
    graph.append(list(map(int,input().split())))

house =[]
chicken = []
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 : # 가정집 
            house.append([i,j])
        elif graph[i][j] == 2 : # 치킨집
            chicken.append([i,j])

result = sys.maxsize
for chi in combinations(chicken,m) :
    temp = 0  # 도시의 치킨거리
    for h in house : # 집을 돌아 
        chi_len = sys.maxsize
        for j in range(m) : # 집마다 가장 가까운 치킨거리를 골라 도시의 치킨거리에 더함 
            chi_len = min(chi_len, abs(chi[j][0] - h[0]) +abs(chi[j][1] - h[1]) )
        temp += chi_len
    result = min(temp , result)

print(result)
