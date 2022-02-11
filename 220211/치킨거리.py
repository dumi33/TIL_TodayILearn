import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int,input().split())
graph = []
house = []
chicken = []
for _ in range(n) :
    graph.append(list(map(int,input().split())))

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 : house.append([i,j]) # 가정집
        elif graph[i][j] == 2 : chicken.append([i,j]) # 치킨집 

result  = sys.maxsize
for chi in combinations(chicken,m) : # chicken집 중에서 m개의 모든 조합 
    city_chi = 0 # 도시의 치킨거리 
    for h in house :
        chi_dis = sys.maxsize
        for j in range(m) :
            chi_dis=min(chi_dis,abs(chicken[j][0] - h[0]) + abs(chicken[j][1] - h[1])) # 집까지의 거리 
        city_chi += chi_dis

    result = min(city_chi, result)
print(result)
