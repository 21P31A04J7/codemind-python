n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in l:
    if i not in range(a,b+1):
        k.append(i)

if len(k)==0:
    print("-1")
else:
    print(min(k))