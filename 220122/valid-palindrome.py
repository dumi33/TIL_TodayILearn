def isPalindrome(self, s: str) -> bool:
        strs = []
        for word in s :
            if word.isalnum() :
                strs.append(word.lower())
        return strs[::-1] == strs # s랑 비교하면 틀림 
         
