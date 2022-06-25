def solution(numbers, target):
    answer = 0
    def dfs(idx, val) :
        
        if idx == len(numbers) :
            nonlocal answer 
            if val == target : answer+=1 
        else :
            dfs(idx+1, val + numbers[idx])
            dfs(idx+1, val - numbers[idx])
    dfs(0,0)  
    return answer
