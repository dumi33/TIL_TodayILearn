from collections import deque 
def solution(begin, target, words):
    answer = 0
    d = deque()
    d.append([begin,0])
    vis = [0 for i in range(len(words))]
    while d :
        word, cnt = d.popleft()
        if word == target :
            answer = cnt
            break 
        for i in range(len(words)) :
            tmp_cnt = 0
            if vis[i] == 0 :
                for j in range(len(word)) :
                    if word[j] != words[i][j] :
                        tmp_cnt+=1 
                if tmp_cnt == 1 :
                    d.append([words[i],cnt+1])
                    vis[i] = 1 
    return answer
