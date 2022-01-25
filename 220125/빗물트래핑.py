def trap(self, height: List[int]) -> int:
        volume = 0
        left,right = 0, len(height)-1
        
        left_max,right_max = height[left],height[right]
        
        while left < right : # 왼쪽과 오른쪽이 같아질 때 까지
            left_max,right_max = max(left_max,height[left]),max(height[right],right_max) # 갱신
            
            if left_max < right_max : # 가장 긴 막대를 찾아야하니까 긴 곳으로 이동
                volume += left_max - height[left]
                left+=1
            else : 
                volume += right_max - height[right]
                right-=1
            
        return volume
