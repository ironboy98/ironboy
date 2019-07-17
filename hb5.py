s=int(input())
hb=list(map(int,input().split(None,s)[:s]))
s=[]
for i in range(len(hb)):
    if hb[i]==i:
        
        s.append(hb[i])
if len(s)==0:
    print(-1)
else:
    print(" ".join(map(str,s)))
