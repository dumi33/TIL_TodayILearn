 def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digits = [],[]
        for log in logs : # 자꾸 for 대신에 if로 잘못쓰고 틀린다
            if log.split()[1].isdigit() :
                digits.append(log)
            else : letter.append(log)
        
        letter.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        return letter + digits
