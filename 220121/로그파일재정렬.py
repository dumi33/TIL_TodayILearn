def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit , letter  = [],[]
        for i in logs :
            if i.split()[1].isdigit() : # 식별자 이후가 숫자라면
                digit.append(i)
            else : letter.append(i)
                
        letter.sort(key = lambda x : (x.split()[1:],x.split()[0] ))
        return letter + digit
        
