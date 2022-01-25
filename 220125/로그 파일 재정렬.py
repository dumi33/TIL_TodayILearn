def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter,digits = [],[]
        for word in logs :
            if word.split()[1].isdigit() : # split()하는거 잊지말기 
                digits.append(word)
            else : letter.append(word)
        
        letter.sort(key=lambda x : (x.split()[1:],x.split()[0])) # return 없음 
        
        
        return letter + digits
