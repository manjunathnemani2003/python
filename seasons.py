from datetime import datetime
import sys
import re
import inflect
p=inflect.engine()

def main():
    #c=input("dob: ")
    print(display("2003-10-07"),end=" ")
    print("minutes broo...")


def display(dob):
   n=datetime.today().date()
   m=n.strftime("%Y-%m-%d")
   ty=m[0]+m[1]+m[2]+m[3]
   tm=m[5]+m[6]
   td=m[8]+m[9]
   try:
    a=re.search(r"(\d\d\d\d)-(\d\d)-(\d\d)",dob)
    b=a.groups()
    if 1<int(b[1])<13 and 0<int(b[2])<32:
        try:
          d1=datetime(int(ty),int(tm),int(td))
          d2=datetime(int(b[0]),int(b[1]),int(b[2]))
          o=(d1-d2).days
          q=int(o)*1440
          r=p.number_to_words(q)
          return r
        except AttributeError:
          sys.exit("invalid date")
    else:
        sys.exit("invalid date")
   except AttributeError:
      sys.exit("invalid date")



if __name__ == "__main__":
    main()
