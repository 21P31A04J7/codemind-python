n=int(input())
l=list(map(int,input().split()))
k=[]
import math
for i in l:
    v=int(math.sqrt(i))
    if v==i/v:
        k.append(i)
print(sum(k))