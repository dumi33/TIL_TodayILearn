## 자꾸 틀린 코드라고 나옴

from itertools import combinations

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 : house.append([i,j])
        elif graph[i][j] == 2 : chicken.append([i,j])

 
ans = sys.maxsize
for ch_addr in combinations(chicken, m) :
    city_chi = 0
    for h in house:
        chick_dis = sys.maxsize
        for j in range(m) :
            chick_dis = min(chick_dis, abs(ch_addr[j][0] - h[0]) + abs(ch_addr[j][1] - h[1]))
        city_chi += chick_dis
    ans = min(ans, city_chi)
print(ans)


