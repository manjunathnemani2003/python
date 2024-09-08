queue=[]
n=0
m=int(input("enter size of list "))

while n<m:

  options=input("""select options: 1-->add
                2-->delete
                3-->exit """)

  #add
  if options=="1":
    temp1=[]
    temp=(input("give the data you want to add: "))

    for i in range(len(queue)):
      temp1.append(queue[i])

    queue.clear()
    queue.append(temp)

    for i in range(len(temp1)):
      queue.append(temp1[i])

  #delete
  if options=="2":
    queue.pop()

  #exit
  if options=="3":
    break

  n=n+1

print(queue)

