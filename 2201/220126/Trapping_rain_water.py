def trap(self, height: List[int]) -> int:
        volume = 0
        left, right = 0, len(height)-1
        
        left_max, right_max = height[left],height[right]
        while left < right :
            left_max, right_max = max(left_max,height[left]), max(right_max,height[right]) #left_max, right_max를 초기화할 때 그냥 left, right이 아니라 height[left], hegith[right]이다.
            
            if left_max < right_max :  # 가장 큰 값을 찾기위해서
                volume += left_max - height[left]
                left += 1
            else : 
                volume += right_max - height[right]
                right -= 1
        return volume
