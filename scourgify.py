import sys
import csv

if len(sys.argv)<3:
  sys.exit("too few command-line arguments")
elif len(sys.argv)>3:
  sys.exit("too many command-line arguments")
elif sys.argv[1].endswith(".csv")==False:
  sys.exit("not a csv file")
else:
  try:
    students=[]
    firstname=[]
    lastname=[]
    house=[]
    a=''
    b=''
    with open(sys.argv[1]) as file:
      reader=csv.DictReader(file)
      for row in reader:
        students.append({"name":row["name"],"house":row["house"]})
      for i in students:
        a,b=i['name'].rstrip().split(',')
        c=i['house']
        house.append(c)
        firstname.append(a)
        lastname.append(b)
    with open(sys.argv[2],'a') as file:
      writer=csv.writer(file)
      for j in range(len(house)):
        writer.writerow([lastname[j],firstname[j],house[j]])

  except FileNotFoundError:
    sys.exit("could not read csv")
