 def longestPalindrome(self, s: str) -> str:
        def palindrom(left, right):    
            while left >= 0 and right < len(s) and s[left] == s[right]: #  while이라는거 유의

                left -= 1
                right += 1
            return s[left+1:right]
        result = ""
        if len(s) < 2 or s == s[::-1]:
            return s


        for i in range(len(s)-1):
            result = max(result, palindrom(i, i+1), palindrom(i, i+2), key = len)
        return result 
