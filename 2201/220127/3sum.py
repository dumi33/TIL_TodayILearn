def threeSum(self, nums: List[int]) -> List[List[int]] :
        ans = []
        nums.sort()
        for i in range(len(nums)-2 ) :
            left, right = i+1, len(nums)-1
            if i > 0 and nums[i]== nums[i-1] : continue # 중복일 경우
            while left < right :
                sum = nums[i] + nums[left] + nums[right] 
                if sum > 0 : right-=1
                elif sum < 0 : left+=1
                else : 
                    ans.append([nums[i],nums[left],nums[right]])
                    
                    while left < right and nums[left] == nums[left+1] : # if 가 아니라 while이다.
                        left+=1
                    while left < right and nums[right] == nums[right-1] :
                        right-=1
                    left += 1
                    right -=1
    
        return ans   
