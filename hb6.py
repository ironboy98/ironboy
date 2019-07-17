N=int(input())
hb1=input(" ")
hb1=list(hb1.split(' '))
c={}
for i in hb1:
   if i in c:
      c[i]+=1
   else:
      c[i]=1
for key,value in c.items():
  if value==1:
     print(key)
