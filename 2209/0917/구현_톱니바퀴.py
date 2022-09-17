# 왼쪽 톱니 확인      
def change_left(num,dir) :
    # 돌릴 수 있다면 
    if num >= 1 and topni[num][2] != topni[num+1][6] :
        change_left(num-1,-dir)
        topni[num].rotate(dir)
    else : return 

def change_right(num,dir) :
    # 돌릴 수 있다면 
    if num <= 4 and topni[num][6] != topni[num-1][2] :
        change_right(num+1,-dir)
        topni[num].rotate(dir)
    else : return 

if __name__=="__main__" :
    topni = {}
    for i in range(1,5) :
        topni[i] = deque(map(int,input()))
        
    n = int(input())
    for i in range(n) :
        num,dir = map(int,input().split())
        # 왼쪽 톱니 확인 
        change_left(num-1,-dir)
        # 오른쪽 톱니확인 
        change_right(num+1,-dir)
        # 내 톱니 돌리기 
        topni[num].rotate(dir)

    
    ans = 0
    for i in range(1,5) :
        ans += topni[i][0] * (2**(i-1))
    print(ans)
