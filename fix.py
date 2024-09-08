a=input('enter infix expression: ')
b=[]

#iterating through all the elements in input
for i in a:

  #if element is a number
  if i.isnumeric():
    print(i,end="")

  #if element is (
  elif i=='(':
    b.append(i)

  #if element is )
  elif i==')':
    for j in range(len(b)):
      if b[-1]=='(':
        break
      print(b[-1],end='')
      b.pop()
    b.remove('(')

  else:
    #if element is +
    if i=='+':
      if len(b)==0:
        b.append(i)
      elif b[-1]=='+' or b[-1]=='*' or b[-1]=='/' or b[-1]=='^':
        while True:
          if len(b)==0:
            b.append(i)
            break
          if b[-1]=='+' or b[-1]=='*' or b[-1]=='/' or b[-1]=='^':
            print(b[-1],end='')
            b.pop()
          elif b[-1]=='-':
            b.append(i)
            break
          else:
            continue
      else:
        b.append(i)

    #if ele is -
    elif i=='-':
      if len(b)==0:
        b.append(i)
      elif b[-1]=='+' or b[-1]=='-' or b[-1]=='*' or b[-1]=='/' or b[-1]=='^':
        while True:
          if len(b)==0:
            b.append(i)
            break
          if b[-1]=='+' or b[-1]=='-' or b[-1]=='*' or b[-1]=='/' or b[-1]=='^':
            print(b[-1],end='')
            b.pop()
          elif b[-1]=='(' or len(b)==0:
            b.append(i)
            break
          else:
            continue
      else:
        b.append(i)

    # if el is *
    elif i=='*':
      if len(b)==0:
        b.append(i)
      elif b[-1]=='*' or b[-1]=='/' or b[-1]=='^':
        while True:
          if len(b)==0:
            b.append(i)
            break
          if b[-1]=='*' or b[-1]=='/' or b[-1]=='^':
            print(b[-1],end='')
            b.pop()
          elif b[-1]=='-' or b[-1]=='+':
            b.append(i)
            break
          else:
            continue
      else:
        b.append(i)

    #if el is /
    elif i=='/':
      if len(b)==0:
        b.append(i)
      elif b[-1]=='*' or b[-1]=='/' or b[-1]=='^':
        while True:
          if len(b)==0:
            b.append(i)
            break
          if b[-1]=='*' or b[-1]=='/' or b[-1]=='^':
            print(b[-1],end='')
            b.pop()
          elif b[-1]=='-' or b[-1]=='+':
            b.append(i)
            break
          else:
            continue
      else:
        b.append(i)

    #if el is ^
    else:
      if len(b)==0:
        b.append(i)
      elif b[-1]=='^':
        print(b[-1],end='')
        b.pop()
        b.append(i)
      else:
        b.append(i)

for k in b:
   print(k,end="")

print()
