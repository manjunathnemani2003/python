def main():
  #these inputs are dummy, the list is what that matters
  '''
  input1=input("enter size of array: ")
  input2=input("enter elements of array: ")
  list=[1,2,3,4,5]
  n=0
  for i in range(1,100):
     for j in range(1,100):
        if hcf(i,j)*lcm(i,j) in list:
           n=n+1
  print(f"the no of pairs are: {n}")
  '''
  hcf(4,2)

def hcf(a,b):
   list=[]
   for i in range(1,1000):
      if a%i==0 and b%i==0:
         list.append(i)
   print(list[len(list)-1])

def lcm(c,d):
  for i in range(1,1000):
    if i%c==0 and i%d==0:
       break
    else:
       continue
  return i


main()
