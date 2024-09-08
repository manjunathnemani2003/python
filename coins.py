coins=[1,4,5]
amount=13

def do(coins,amount):
  c=0
  i=1
  if amount==0:
    return 0
  try:
    while True:
      if amount-coins[-i]>=0:
        c=c+1
      amount=amount-coins[-i]
      #print(f'before compensation: {amount}')
      if amount<0:
        amount=amount+coins[-i]
        #print(f'after compensation: {amount}')
        i=i+1
        if amount==0:
          return c
  except:
    return -1

print(do(coins,amount))
