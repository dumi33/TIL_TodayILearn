def isPalindrome(self, s: str) -> bool:
        words = re.sub(r'[^A-Za-z0-9]','',s).lower() # 정규표현식 주의
        return words==words[::-1]
