def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range (len(nums)-2) :
            if i > 0 and nums[i] == nums[i-1] : # 중복일 경우 pass
                continue
            left, right = i +1, len(nums)-1
            while left < right :
                sum = nums[left] + nums[right] + nums[i]
                if sum > 0 : right -=1
                if sum < 0 : left += 1 # if 면 틀린다 
                if sum==0 : # sum == 0 일 때 # 3개 다 if면 맞는다. 
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1] : left+=1 # if가 아니라 while
                    while left < right and nums[right] == nums[right-1] : right-=1
                    left += 1
                    right -= 1
                        
        return result
