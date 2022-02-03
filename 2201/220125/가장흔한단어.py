def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ',paragraph) #  ''가 잘 끝났는지 확인하기 # 변수명이 중복되지않았는지 확인하기
                .lower().split()
                if word not in banned]
        ans = collections.Counter(words) # words는 리스트 형태 
        return ans.most_common(1)[0][0]
