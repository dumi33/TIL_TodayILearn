def trap(self, height: List[int]) -> int:
        left,right = 0, len(height)-1
        left_max , right_max = height[left], height[right]
        volume = 0
        while left < right :
            left_max , right_max= max(height[left], left_max) ,max(height[right], right_max)
            if right_max < left_max : # 가장 높은 블럭을 찾기위해서 # left가 높으니 right이 이동
                volume += right_max - height[right]
                right -=1 
                
            else :
                volume += left_max - height[left]
                left +=1
        return volume 
