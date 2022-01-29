def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        p = 1
        for i in range(len(nums)) : # 왼쪽 곱을 ans 에 저장
            ans.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums)-1, -1,-1) : # 역방향으로 진행하면서 ans에 오른쪽 곱을 곱한다.
            ans[i] = ans[i] * p
            p *= nums[i]
        
        return ans
