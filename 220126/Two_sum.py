def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = {}
        for i, num in enumerate(nums) :
            diction[num] = i
        
        for i, num in enumerate(nums) :
            if target-num in diction and i != diction[target-num] :
                return i, diction[target-num]
