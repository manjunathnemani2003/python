def main():
    print(value(" Hello "))


def value(greeting):
    m=greeting.lower()
    n=m.strip()
    if len(n)>4:
        if n[0]+n[1]+n[2]+n[3]+n[4]=="hello":
            return "$0"
        elif n[0]=="h":
          return "$20"
        else:
            return "$100"
    else:
        if n[0]=="h":
          return "$20"
        else:
          return "$100"

if __name__ == "__main__":
    main()
