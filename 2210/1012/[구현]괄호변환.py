def divide(p) :
    openCnt = 0
    closeCnt = 0
    for i in range(len(p)) :
        if p[i]=='(': openCnt+=1 
        else : closeCnt +=1 
        if closeCnt == openCnt : 
            return p[:i+1],p[i+1:]
        
def check(p) :
    stack = []
    for i in p :
        if i =='(' :
            stack.append(i)
        else :
            if len(stack)==0 : return False 
            stack.pop(0)
    return True 


def solution(p) :
    if not p : return ""
    u,v = divide(p)
    
    if check(u) :
        return u + solution(v)
    else :
        answer = '('
        answer += solution(v)
        answer += ')'
        for i in u[1:len(u)-1] :
            if i == '(' :
                answer += ')'
            else : answer += '('
        return answer
