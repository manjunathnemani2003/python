import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    c=re.sub("com","be",s)
    a=re.search(r'<iframe src="((https?://(www.)?.+)\.(.+)embed/(.+))"></iframe>',c)
    b=a.groups()
    if a.group(1):
      print(b[2]+"."+b[4]+b[5])
    else:
        return None

 #<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

if __name__ == "__main__":
    main()

