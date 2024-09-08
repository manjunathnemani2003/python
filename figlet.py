import sys
from pyfiglet import Figlet
from random import choice

if len(sys.argv)>1:
  if sys.argv[1]=="-f" or sys.argv[1]=="--font":
    if sys.argv[2] in Figlet().getFonts():
      figlet = Figlet()
      figlet.getFonts()
      figlet.setFont(font=sys.argv[2])
      s=input("input: ")
      print(figlet.renderText(s))
    else:
      sys.exit("invalid input")
  else:
    sys.exit("invalid input")

elif sys.argv[0]=="figlet.py":
  s=input("input: ")
  figlet = Figlet()
  f=choice(figlet.getFonts())
  figlet.setFont(font=f)
  print(figlet.renderText(s))

else:
  sys.exit(1)

