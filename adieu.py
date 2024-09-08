m=[]
while True:
 try:
    n=input("name: ")
    m.append(n)
 except EOFError:
    print()
    break
print("Adieu, adieu, to ",end="")

if len(m)>1:
  for i in range(len(m)-1):
    print(m[i] ,end="")
    if i!=len(n)-1:
      print(", ",end="")
    else:
      break
  print(f"and {m[len(m)-1]}")

if len(m)==1:
  print(m[0])


