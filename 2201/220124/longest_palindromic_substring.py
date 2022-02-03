def longestPalindrome(self, s: str) -> str:
        
        def Palin(left : int, right :int) -> str :
            while left >= 0 and right < len(s) and s[left]==s[right] : # 영역에서 벗어나지 않고 팰린드롬인동안
                left-=1 # 영역 넓히기
                right+=1
            return s[left+1:right] # 어차피 right은 -1 까지만 나오므로 -1을 할 필요가 없음
        
        if len(s)<2 or s==s[::-1] : return s
        
        
        ans = ""
        for i in range(len(s)-1) :
            ans = max(ans,Palin(i,i+1),Palin(i,i+2),key = len)
        
        return ans
