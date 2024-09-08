arr=[7,1,3,5,2,6,4]
m=float('inf')
n=[]
for i in range(len(arr)):
  for j in range(i+1,len(arr)):
    if arr[j]<m:
      m=arr[j]
      n.append(j)
    else:
      continue
  if arr[i]>arr[n[-1]]:
    arr[i],arr[n[-1]]=arr[n[-1]],arr[i]
  else:
    continue
  if i==len(arr)-1:
    break
  else:
    m=float('inf')

print(arr)




