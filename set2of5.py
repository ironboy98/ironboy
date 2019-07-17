hb1=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']
hb2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
hb3=str(input())
for hb4 in range(20):
  if(hb3==hb1[hb4]):
    print(hb2[hb4])
    break
