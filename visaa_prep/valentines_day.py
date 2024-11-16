x,y=map(int,input().split())
m=0
for i in range(x):
    if y*i<=x:
        m=max(m,i)
print(m)
