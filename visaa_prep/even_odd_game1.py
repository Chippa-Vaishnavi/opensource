number=int(input())
s=str(number)
sum=0
for i in range(0,len(s)):
    sum+=int(s[i])
if sum%2==0:
    print("Vignesh")
else:
    print("Charan")
