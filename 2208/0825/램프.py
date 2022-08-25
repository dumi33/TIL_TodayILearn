def solve() :
    answer = 0
    # 행을 돌면서 
    for i in mp :
    	# 0의 개수를 구한다. 
        zero_cnt = i.count(0)
        # 0의 개수가 k보다 작거나 같고 홀수면 홀수, 짝수면 짝수라면 
        if zero_cnt <= k and zero_cnt%2 == k%2 :
            cnt = 0
            # 행을 다시 돌면서 동일한 값의 행의 개수를 구한다. 
            for j in mp :
                if j == i : cnt+=1 
            # 최대값을 갱신한다. 
            answer = max(answer,cnt)
    return answer

if __name__=="__main__" :
    n,m = map(int,input().split())
    mp = [list(map(int,input())) for _ in range(n)]
    k = int(input())
    print(solve())
