from collections import deque 
def solution(begin, target, words):
    answer = 0
    vis = [0 for i in range(len(words))]
    q =deque()
    q.append([begin,0])
    
    while q:
        word, cnt = q.popleft()
        if word == target :
            return cnt
        for i in range(len(words)) :
            if vis[i] == 0:
                tmp_cnt = 0
                for j in range(len(word)) :
                    if word[j] != words[i][j] :
                        tmp_cnt+=1
                if tmp_cnt == 1 :
                    q.append([words[i],cnt+1])
                    vis[i] = 1 
    return answer
