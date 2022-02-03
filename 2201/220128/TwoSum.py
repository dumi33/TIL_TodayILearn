 def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = {}
        for i,value in enumerate(nums) :
             diction[value] = i
        
        for index, value in enumerate(nums) :
            if target - value in diction and index != diction[target - value] :
                return index, diction[target-value]
