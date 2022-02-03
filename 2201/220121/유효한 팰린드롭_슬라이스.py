import re
def isPalindrome(self, s: str) -> bool:
        s= s.lower() # 소문자로
        s = re.sub('[^a-z0-9]','',s)
        return s[::-1] == s
