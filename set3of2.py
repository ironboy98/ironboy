hb=int(input())
n=list(map(int,input().split(None,hb)[:hb]))
n.sort(key=None,reverse=True)
if n.count(0)==len(n):
    print(0)
else:
    print("".join(map(str,n)))
