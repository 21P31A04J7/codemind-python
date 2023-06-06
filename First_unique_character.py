n=input().lower()
l=[]
for i in n:
    if 1!=' ' and n.count(i)==1:
        l.append(i)
if len(l)==0:
    print("-1")
else:
    print(l[0])