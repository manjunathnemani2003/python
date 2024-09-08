coins=[1,4,5]
amount=13
m=0

dic={
  0:0
}

for i in range(1,amount+1):
  for j in range(1,len(coins)+1):
    if coins[-j]<=i:
      m=i-coins[-j]
      if m==0:
        dic[i]=1
      elif m>j:
        dic[i]=1+dic[i-coins[-j]]

print(dic)

