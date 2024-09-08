m=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
o=""
while True:
  n=input("Date: ")

  #if date and month are single digit
  if n[1]=="/" and n[3]=="/":
    print(f"{n[-4]+n[-3]+n[-2]+n[-1]}-0{n[0]}-0{n[2]}")
    break
  #if month is double digit & date-sd
  elif n[2]=="/" and n[4]=="/" and 0<int(n[0]+n[1])<13:
    print(f"{n[-4]+n[-3]+n[-2]+n[-1]}-{n[0]+n[1]}-0{n[3]}")
    break
  #if date is dd and m-sd
  elif n[4]=="/" and n[1]=="/" and 0<int(n[2]+n[3])<32:
    print(f"{n[-4]+n[-3]+n[-2]+n[-1]}-0{n[0]}-{n[2]+n[3]}")
    break
  #if date & m are dd
  elif n[5]=="/" and n[2]=="/" and 0<int(n[0]+n[1])<13 and 0<int(n[3]+n[4])<32:
    print(f"{n[-4]+n[-3]+n[-2]+n[-1]}-{n[0]+n[1]}-{n[3]+n[4]}")
    break
  #if we enter month in alphabets
  elif len(n)>10:
      if n[-6]==",":
        for i in range(len(n)):
          if n[i]==" ":
            break
          o=o+n[i]
        if o in m:

          if n[-8]==" ":
            if m.index(o)+1<10:
              print(f"{n[-4]+n[-3]+n[-2]+n[-1]}-0{(m.index(o))+1}-0{n[-7]}")
              break
            else:
              print(f"{n[-4]+n[-3]+n[-2]+n[-1]}-{(m.index(o))+1}-0{n[-7]}")

          elif 0<int(n[-8]+n[-7])<32:
            if m.index(o)+1<10:
              print(f"{n[-4]+n[-3]+n[-2]+n[-1]}-0{(m.index(o))+1}-{n[-8]+n[-7]}")
              break
            else:
              print(f"{n[-4]+n[-3]+n[-2]+n[-1]}-{(m.index(o))+1}-{n[-8]+n[-7]}")
          else:
            continue
      else:
        continue
  else:
    continue









