def solution(number, k):
    arr = []
    for n in number :
        while k and arr and arr[-1] < n :
            arr.pop()
            k-=1
        arr.append(n)
        
    return (''.join(arr))[:-k]
