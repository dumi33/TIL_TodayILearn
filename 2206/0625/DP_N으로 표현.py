def solution(N, number):
    dp = []
    for i in range(1,9) :
        all_case = set()
        all_case.add(int(str(N)*i))
        
        for j in range(i-1) :
            for op1 in dp[j] :
                for op2 in dp[-j-1] :
                    all_case.add(op1+op2)
                    all_case.add(op1-op2)
                    all_case.add(op1*op2)
                    if op2!=0 :
                        all_case.add(op1//op2)
        if number in all_case :
            return i
        dp.append(all_case)
    return -1
