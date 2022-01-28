def threeSum(self, nums: List[int]) -> List[List[int]] :
        nums.sort()
        ans = []
        for i in range(len(nums)-2) : # i의 범위는 left , right이 존재할 수 있을만큼
            if i >0 and nums[i] == nums[i-1] : continue
                
            left, right = i+1, len(nums)-1
            while left < right :
                sum = nums[left] + nums[right] + nums[i] 
                if sum < 0 : left += 1
                elif sum > 0 : right -=1 
                else : # 스펠링 틀렸었다. 
                    ans.append([nums[i],nums[left],nums[right]]) # 3개의 수를 하나에 집어넣는다.
                    
                    while (left) < right and nums[left] == nums[left +1 ] : left +=1
                        
                    while (right) > left and nums[right] == nums[right -1 ] : right -=1
                    
                    left += 1
                    right -=1 
        return ans
