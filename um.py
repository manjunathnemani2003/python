import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    a=re.findall(r"\bum\b",s,re.IGNORECASE)
    return len(a)

if __name__ == "__main__":
    main()

#text = "He was carefully disguised but captured quickly by police."
#re.findall(r"\w+ly\b", text)
