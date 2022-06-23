from collections import defaultdict
def solution(n, results):
    answer = 0
    lose_set = defaultdict(set)
    win_set = defaultdict(set)

    for win,lose in results :
        lose_set[win].add(lose)
        win_set[lose].add(win)
    
    for i in range(1,n+1) :
        for win in win_set[i] :
            lose_set[win].update(lose_set[i])
        for lose in lose_set[i] :
            win_set[lose].update(win_set[i])
    for i in range(1,n+1) :
        if (len(win_set[i]) + len(lose_set[i]) == n-1) :
            answer += 1
        
        
    return answer
