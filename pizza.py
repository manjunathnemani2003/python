import sys
import csv
from tabulate import tabulate

if len(sys.argv)<2:
  sys.exit("too few command-line arguments")
elif len(sys.argv)>2:
  sys.exit("too many command-line arguments")
elif sys.argv[1].endswith(".csv")==False:
  sys.exit("not a csv file")
else:
  try:
    a=[]
    b=[]
    with open(sys.argv[1]) as file:
      for line in file:
        x,y,z=line.rstrip().split(",")
        b.append(x)
        b.append(y)
        b.append(z)

        for i in file:
          d,e,f=i.rstrip().split(",")
          a.append([d,e,f])
        print(tabulate(a,b,tablefmt="github"))

  except FileNotFoundError:
    sys.exit("File does not exit")
