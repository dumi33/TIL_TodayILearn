def dfs(x) :
    if x > 7 :
        return
    else :
        print(x,end=' ')
        dfs(x*2)
        dfs(x*2+1)
        
if __name__=="__main__" : 
    dfs(1)
