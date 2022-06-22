def solution(N, number):
    answer = -1
    dp = []
    for i in range(1,9) :
        all_case = set()
        all_case.add(int(str(N)*i))
        for j in range(0,i-1) :
            for oper1 in dp[j] :
                for oper2 in dp[-j-1] :
                    all_case.add(oper1 + oper2)
                    all_case.add(oper1 - oper2)
                    all_case.add(oper1 * oper2)
                    if oper2 != 0 :
                        all_case.add(oper1 // oper2)
        if number in all_case :
            answer = i
            break
        dp.append(all_case)
                    
    return answer
