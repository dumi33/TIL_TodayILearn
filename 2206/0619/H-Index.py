def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i, v in enumerate(citations) :
        if i >=v :
            return i
    return len(citations)
