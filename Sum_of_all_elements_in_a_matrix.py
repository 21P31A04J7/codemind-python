r,c=map(int,input().split())
mat=[]
s=0
for i in range(r):
    n=list(map(int,input().split()))
    mat.append(n)
for i in mat:
    for j in i:
        s=s+j
print(s)