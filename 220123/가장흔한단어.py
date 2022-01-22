def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words =[word for word in re.sub(r'[^\w]',' ',paragraph)
                .lower().split()
                    if word not in banned]

        ans = collections.Counter(words) # 값과 빈도수의 리스트를 만든다.
        return(ans.most_common(1)[0][0]) # 가장 많은 빈도의 값을 반
