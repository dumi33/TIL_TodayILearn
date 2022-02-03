def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s :
            if char.isalnum() : # 영어, 한글만 
                strs.append(char.lower())
                
        word2 = strs[::-1]
        return word2 == strs


