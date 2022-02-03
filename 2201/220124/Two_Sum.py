def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {} # 딕셔너리 생성
        for i, num in enumerate(nums) :
            nums_map[num] = i
        
        for i, num in enumerate(nums) :
            if target - num in nums_map and i != nums_map[target-num] :
                return nums.index(num), nums_map[target-num]
