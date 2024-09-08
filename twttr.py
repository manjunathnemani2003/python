def main():
    print(shorten("hey! how are you maaan!!!"))

def shorten(word):
    r=""
    p=word.lower()
    for i in range(len(p)):
        if word[i]=="a" or word[i]=="e" or word[i]=="o" or word[i]=="u" or word[i]=="i":
            continue
        else:
            r=r+word[i]
    return r

if __name__ == "__main__":
    main()
