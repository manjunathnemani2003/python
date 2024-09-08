n=int(input('enter height of pyramid: '))
m=1
def pyr(c,m):
  for _ in range(m):
    print("+",end='')
    c=c+1
  print()
  if c==n:
    return 1
  else:
    pyr(0,m+1)

pyr(0,m)
