def longestPalindrome(self, s: str) -> str:
        ans = ""
        def palin(left : int , right :int) -> str :
            while left >= 0 and right < len(s) and s[left] == s[right]: # = 붙는거 생각 잘하기 
                left -= 1
                right +=1
            
            return s[left+1 : right] 
        if len(s) <2 or s == s[::-1] : return s # 잊어버리지마
        for i in range(len(s)-1) :
            ans = max(ans, palin(i,i+1),palin(i,i+2), key = len)
        
        return ans
