from collections import Counter
def solution(clothes):
    answer = 1
    arr = []
    for name, types in clothes :
        arr.append(types)
    arr=Counter(arr)
    for i in arr.values() :
        answer *= (i+1)
    return answer-1
