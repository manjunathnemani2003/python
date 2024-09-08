def fib(n):
  #[1,2,3,4,5]
  #[0,1,1,2,3,5,8,13,21,44]
  s=[0,1]
  sum=0
  for i in range(2,n):
    sum=s[-1]+s[-2]
    s.append(sum)
  return s[-1]

print(fib(50))
