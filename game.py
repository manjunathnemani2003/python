from random import randint

while True:
  n=input("level: ")
  if n.isdigit():
    if int(n)>0:
      break
    else:
      continue
  else:
    continue
while True:
  m=input("guess: ")
  if m.isdigit():
    if int(m)>0:
      break
    else:
      continue
  else:
    continue
o=randint(1,int(n))
if int(m)>o:
  print("Too large!")
elif int(m)<o:
  print("Too small!")
else:
  print("Just Right!")
