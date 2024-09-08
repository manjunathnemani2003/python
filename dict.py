wordDict = ["cats","dog"]
s = "catsandog"
c=0
n=[]
m=[]
d=0
for i in s:
  n.append(i)
for j in wordDict:
  for i in j:
    m.append(i)
    c=c+1

for i in m:
  if i in n:
    n.remove(i)
    d=d+1

if c==d:
  print(n)
  print('true')
else:
  print('false')
