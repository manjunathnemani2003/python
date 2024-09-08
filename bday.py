n=int(input("max value "))
k=int(input("len of array "))
m=[]
p=[]

#creating a function which stores all the possible combinations of arrays in a list based on given inputs

def iter(c,n,mn,d,p):
  if n==d:
    p.append(c)
    return
  for i in range(1,mn+1):
    iter(c+[i],n,mn,d+1,p)

# this function check whether an array satisfy given condition or not

def condition(arr):
    v=0
    if len(arr)==2:
        if arr[1]%arr[0]==0:
            return True
    if len(arr)>2:
      for i in range(1,len(arr)):
          if arr[i]%arr[i-1]==0:
              v=v+1
          else:
              return False
    if v==len(arr)-1:
        return True

#we then give all the possible arrays as inputs to the above function which checks validity. if the array is valid, it increases count

count=0
c=0
iter(m,k,n,0,p)
for i in p:
  #print(i)
  for j in i:
    #print(f"{j} compare {n}")
    if j<n or j==n:
      c=c+1
  if c==k:
    if condition(i)==True:
      print(f"combination {i} is valid")
      count=count+1
  c=0

# this is if the given array size is 1 :)
if k==1:
  count=n

#prints total possible combinations

print(f"total combinations: {count}")










