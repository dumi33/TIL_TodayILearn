import sys
input = sys.stdin.readline

H,W = map(int,input().split())
height = list(map(int, input().split())) # 잊어먹었었다. 

volume = 0
left, right = 0, len(height)-1
left_max, right_max = height[left],height[right]

while left < right : 
    left_max ,right_max = max(height[left],left_max),max(height[right],right_max)

    if left_max < right_max : # 가장 긴 막대에서 만나기 위해 
        volume += left_max - height[left]
        left += 1 # 오른쪽으로
    else :
        volume += right_max - height[right]
        right -= 1 # 왼쪽으로
    
print(volume)
