from random import randint
q=0
score=0
s=0

while True:
  n=input("Level: ")
  if n=='1' or n=='2' or n=='3':
    break
  else:
    continue

#for level 1
if n=="1":
  while s<10:
    m=randint(0,9)
    o=randint(0,9)
    p=input(f"{m}+{o}=")
    if p!=str(m+o):
       print("EEE")
       while q<2:
         z=input(f"{m}+{o}=")
         if z==str(m+o):
          break
         else:
           print("EEE")
         q=q+1
         if q!=3:
           continue
         else:
           break
       print(f"{m}+{o}={m+o}")
    else:
      score=score+1
    s=s+1
  print(f"score={score}")

#for level 2
elif n=="2":
  while s<10:
    m=randint(10,99)
    o=randint(10,99)
    p=input(f"{m}+{o}= ")
    if p!=str(m+o):
       print("EEE")
       while q<2:
         z=input(f"{m}+{o}=")
         if z==str(m+o):
          break
         else:
           print("EEE")
         q=q+1
         if q!=3:
           continue
         else:
           break
       print(f"{m}+{o}={m+o}")
    else:
      score=score+1
    s=s+1
  print(f"score={score}")

#for level 3
elif n=="3":
  while s<10:
    m=randint(100,999)
    o=randint(100,999)
    p=input(f"{m}+{o}= ")
    if p!=str(m+o):
       print("EEE")
       while q<2:
         z=input(f"{m}+{o}=")
         if z==str(m+o):
          break
         else:
           print("EEE")
         q=q+1
         if q!=3:
           continue
         else:
           break
       print(f"{m}+{o}={m+o}")
    else:
      score=score+1
    s=s+1
  print(f"score={score}")
