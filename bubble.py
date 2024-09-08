arr=[7,1,3,5,2,6,4]
j=0
swaps=0
while j<len(arr):
  for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
      arr[i],arr[i+1]=arr[i+1],arr[i]
      swaps=swaps+1
  if swaps==0:
    break
  swap=0
  j=j+1

print(arr)
