class add:
  def __init__(self,current,next=None):
    self.cv=current
    self.next=next

  def __str__(self):
    return str(self.cv)

n=[]
m=input("enter your numbers size: ")
for i in range(1,int(m)+1):
  j=int(input(f"enter number {i}: "))
  n.append(j)

p=[]
for i in range(len(n)):
  p.append(add(n[i]))

for i in range(len(p)-1):
  p[i].next=p[i+1]

c=p[0]
while True:
  print(c.cv,end=" ")
  if c.next==None:
    print('-->',None)
    break
  print('-->',end=" ")
  c=c.next



