r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
s=0
for i in range(r):
    for j in range(c):
        if i!=0 and j!=0 and i!=r-1 and j!=c-1:
            s=s+m[i][j]
print(s)