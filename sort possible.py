m=[]
nums=[9,2,4]
for i in nums:
  m.append(i)
nums.sort()


c=0
i=0
while True:
  if m==nums:
    print('y')
    break
  else:
    n=m[i]
    m.remove(n)
    m.append(n)
    c=c+1
    if m==nums:
      print('y')
      break
    else:
      i=0
    n=0
  if c==len(m):
    break
if m!=nums:
  print('n')
