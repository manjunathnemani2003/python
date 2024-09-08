arr=[1,100,1,1,1,100,1]
arr.append(0)
cost=0
minc=0

for i in range(len(arr)-1):
  if arr[-i]>arr[-i-1]:
    cost=cost+arr[-i-1]
  else:
    cost=cost+arr[-i]

print(cost)

