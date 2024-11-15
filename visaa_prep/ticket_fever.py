t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    if m-n<=0:
        print("0")
    else:
        print(m-n)
