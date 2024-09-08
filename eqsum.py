n=[14,9,8,4,3,2]

def part(n):
  sums=int(sum(n)/2)
  #print(sums)
  if sum(n)%2!=0:
    return False
  m=0
  c=0
  for i in range(len(n)):
    m=n[i]
    for j in range(i+1,len(n)):
      if i!=j:
        #print(m+n[j],sums)
        if m+n[j]<sums or m+n[j]==sums:
          m=m+n[j]
          c=c+1
        #print(m)
        if m==sums and c<len(n):
          #print(sums,c)
          return True
  return False

print(part(n))



