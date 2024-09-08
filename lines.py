import sys

if len(sys.argv)<2:
  sys.exit("Too few command-line arguements")
elif len(sys.argv)>2:
  sys.exit("Too many command-line arguements")
elif sys.argv[1].endswith(".py")==False:
  sys.exit("not a python file")
else:
  try:
    m=0
    with open(sys.argv[1],"r") as file:
      n=file.readlines()
    for i in n:
      p=i.lstrip()
      if i.strip()=="" or p.startswith("#"):
        continue
      else:
        m=m+1

    print(m)

  except FileNotFoundError:
    sys.exit("File does not exit")
