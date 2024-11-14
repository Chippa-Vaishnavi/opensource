v,c,r,n=list(map(int,input().split()))
if v+c>=n or c+r>=n or v+r>=n:
    print("YES")
else:
    print("NO")
