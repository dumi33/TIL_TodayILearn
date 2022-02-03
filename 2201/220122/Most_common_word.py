 def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ',paragraph)
                .lower().split()
                    if word not in banned]
                                         
        answer = collections.Counter(words) #  딕셔너리 형태로 반환
        return answer.most_common(1)[0][0] # 가장 빈도가 높은 한개만 추출 #빈도가 아닌 값을 반환
