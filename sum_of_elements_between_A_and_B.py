n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in l:
    if i>=a and i<=b:
        k.append(i)
if len(l)==k:
    print("-1")
else:
    print(sum(k))