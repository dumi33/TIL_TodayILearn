def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        p=1
        for i in range(len(nums)) :
            ans.append(p) 
            p*=nums[i]
        p = 1
        for i in range(len(nums)-1,-1,-1) : # 마지막에서 0까지 # ragne의 구분기호는 : 가 아니라, 다.
            ans[i] = ans[i]*p
            p*=nums[i]
        return ans
