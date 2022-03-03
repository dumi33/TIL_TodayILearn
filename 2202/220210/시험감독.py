n = int(input())
arr = list(map(int,input().split()))
b,c = map(int,input().split())

cnt = 0
for student in arr :
    cnt+=1
    if student <= b :  # 감독 한명으로 충분 
        continue
    else :
        if (student-b) % c == 0 :
            cnt += (student-b) // c
        else :
            cnt += (student-b) // c
            cnt += 1
    
print(cnt)
