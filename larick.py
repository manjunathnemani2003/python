arr=[1,1,1,1,2,2,2]
c=0
i=0
n=[]
max=0
element=0

while i<len(arr):
  for j in range(len(arr)):
    if i!=j:
      if arr[i]==arr[j]:
        c=c+1
  if c>max:
    max=c
    element=arr[i]
  c=0
  i=i+1

print(element)
