x,y,z=list(map(int,input().split()))
if x+y<=z:
    print("2")
elif x+y>z and x<=z:
    print("1")
else:
    print("0")
