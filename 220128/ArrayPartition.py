def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans =0
        for i, value in enumerate(nums) :
            if i%2 == 0 : ans+= value  # 0%2 == 0 이다!
                
        return ans
