a=input()
hb=len(a)
c="".join(a[i:i+2][::-1] for i in range (0,hb,2))
print (c)
