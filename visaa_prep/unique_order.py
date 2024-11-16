n=int(input())
arr=list(map(int,input().split()))
uniq=[]
for i in arr:
    if i not in uniq:
        uniq.append(i)
print(" ".join(map(str,uniq)))
