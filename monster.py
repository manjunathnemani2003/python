nom=int(input(""))
iexp=int(input(""))
pom=[]
bom=[]
for i in range(nom):
  n=int(input(""))
  pom.append(n)
for j in range(nom):
  m=int(input(""))
  bom.append(m)

#pom=[101,100,304]
#bom=[100,1,524]
count=0
i=0
while i<len(pom):
  if iexp>pom[i] or iexp==pom[i]:
    iexp=iexp+bom[i]
    count=count+1
    pom.remove(pom[i])
    bom.remove(bom[i])
    i=0
  else:
    i=i+1
print(count)



