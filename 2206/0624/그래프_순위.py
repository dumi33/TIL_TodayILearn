from collections import defaultdict
def solution(n, results):
    answer = 0
    win_set = defaultdict(set)
    lose_set = defaultdict(set)
    
    for win, lose in results :
        win_set[lose].add(win)
        lose_set[win].add(lose)
    
    for i in range(1,n+1) :
        for winner in win_set[i] :
            lose_set[winner].update(lose_set[i])
        for loser in lose_set[i] :
            win_set[loser].update(win_set[i])
            
    for i in range(1,n+1) :
        if len(lose_set[i]) + len(win_set[i]) == n-1 :
            answer += 1
    return answer
