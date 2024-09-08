list=[1,3,4,8]
n=[]
m=[]
k=0
l=0

for i in range(len(list)):
  for j in range(len(list)):
    if i!=j:
      n.append(abs(list[j]-list[i]))
    else:
      continue

for i in range(len(n)):
  for j in range(1,int(len(n)/(len(list)-1))+1):
    if i==(len(n)/len(list))*j:
      m.append(k)
      k=0
  k=k+n[i]

if len(n)>6:
  for i in range(len(n)-3,len(n)):
    l=l+n[i]
    if i==len(n)-1:
      m.append(l)
else:
  p=abs(list[2]-list[1])+abs(list[2]-list[0])
  m.append(p)

print(m)



