def solution(n, k):
    word = ""
    while n :
        word = str(n%k) + word
        n = n//k
    
    word = word.split('0')
    cnt = 0
    for w in word :
        # 빈공간이라면
        if len(w) == 0 : continue 
        # 0 또는 1이라면 
        if int(w) < 2 : continue 
        
        # 소수 찾기 
        sosu = True 
        for i in range(2,int(int(w)**0.5)+1 ) :
            if int(w) % i==0 :
                sosu = False 
                break
        if sosu : cnt+=1 
    
    return cnt
