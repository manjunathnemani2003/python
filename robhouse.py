arr=[1,2,3,10,1,2,3]
cost1=0
cost2=0

for i in arr:
  print(i+cost1,cost2)
  temp=max(i+cost1,cost2)
  cost1=cost2
  cost2=temp
  print(temp)
print(cost2)
