n,m=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
c=0
c1=[]
for i in n:
    if i in m:
        if i not in c1:
            c1.append(i)
print(len(c1))