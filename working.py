import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
     a=re.search(r"^(\d|\d\d)(\:)?(\d\d)? (AM|PM) to (\d|\d\d)(\:)?(\d\d)? (PM|AM)$",s)
     b=a.groups()
     if b[3]=="AM":
        if b[5]!=None and b[1]!=None:
            if 0<=int(b[2])<60 and 0<=int(b[6])<60:
                print(f"{int(b[0]):02}{b[1]+b[2]} to {int(b[4])+int(12)}{b[5]+b[6]}")
        elif b[5]==None and b[1]==None:
             print(f"{int(b[0]):02}:00 to {int(b[4])+int(12)}:00")
        elif b[1]==None and b[2]==None:
             if 0<=int(b[4])<60:
                print(f"{int(b[0]):02}:00 to {int(b[4])+int(12)}{b[5]+b[6]}")
        elif b[5]==None or b[6]==None:
             if 0<=int(b[2])<60:
                print(f"{int(b[0]):02}{b[1]+b[2]} to {int(b[4]):02}:00")

#SIMILARLY WE CAN DO FOR FIRST PM THEN AM CASE AS WELL
#ALSO KEEP AN IF (LIMIT FOR HOURS NOT > 12)
#SO I'M LEAVING THIS PROGRAM, BUT U KNOW WHAT TO DO

if __name__ == "__main__":
    main()
