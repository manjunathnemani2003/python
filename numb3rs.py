import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    #validate("1.2.3.4")


def validate(ip):
    if re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip):
        m=re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)",ip)
        n=m.groups()
        if n[0].isdigit() and n[1].isdigit() and n[2].isdigit() and n[3].isdigit():
          if 0<=int(n[0])<256 and 0<=int(n[1])<256 and 0<=int(n[2])<256 and 0<=int(n[3])<256:
            return True
          else:
            return False
        else:
          return False
    else:
        return False


    #if re.search(r"^.+\..+\..+\..+$",ip):
     #   return True
    #else:
     #   return False

if __name__ == "__main__":
    main()
