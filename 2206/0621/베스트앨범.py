def solution(genres, plays):
    answer = []
    playdic = {}
    dic = {}
    for i, (g,p) in enumerate(zip(genres, plays)) :
        if g in playdic.keys() :
            playdic[g]+=p
            dic[g].append((p,i))
        else :
            playdic[g] = p
            dic[g] = [(p,i)]
    playdic = sorted(playdic.items(),key = lambda x : x[1],reverse = True)
    print(dic)
    for key in playdic :
        playlist = dic[key[0]]
        playlist.sort(key = lambda x : x[0],reverse = True)
        for i in range(len(playlist)):
            if i == 2 :
                break
            answer.append(playlist[i][1])
            
        
    return answer
