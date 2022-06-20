answer = 0

def solution(numbers, target):
    def dfs(idx,val) :
        global answer
        if idx == len(numbers) :
            if val == target :
                answer +=1
                return 
        else :
            dfs(idx+1, val+numbers[idx])
            dfs(idx+1, val-numbers[idx])
    dfs(0,0)
    return answer
