import re
a=input("enter the array ")
b=[]
c=''
d=0
e=[]
g=[]

for i in a:
  if i==" ":
    b.append(int(c))
    c=''
  else:
    c=c+i
b.append(int(c))

def xor(b1,b2):
# Ensure both binary numbers are the same length by padding with leading zeros
  max_len = max(len(b1), len(b2))
  b1 = b1.zfill(max_len)
  b2 = b2.zfill(max_len)
# Perform XOR operation
  result = ''
  for b11, b22 in zip(b1, b2):
    # XOR each bit and append the result to the result string
    result += str(int(b11) ^ int(b22))
  return result

for j in b:
  d=bin(j)
  e.append(d)

for i in e:
  f=re.sub("0b","",i)
  g.append(f)


r=g[0]
for i in range(1,len(g)):
  r=xor(r,g[i])

p=0
for j in r:
  p=p+int(j)

m=0
if p!=0:
  while b[1]!=0:
    b[1]=b[1]-1
    m=m+1
    for j in b:
      d=bin(j)
      e.append(d)
    for i in e:
      f=re.sub("0b","",i)
      g.append(f)
    r=g[0]
    for i in range(1,len(g)):
      r=xor(r,g[i])
    p=0
    for j in r:
      p=p+int(j)
    if p==0:
      print(m)
      break
    elif b[1]==0 and p!=0:
      print("-1")
      break
    else:
      continue
else:
  print("0")



