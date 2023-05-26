n=int(input())
d=len(str(n))
count=0
sum=0
for i in str(n):
    count+=1
    for j in range(count,n+1):
        sum+=int(i)**j
        break
if n==sum:
    print("True")
else:
    print("False")