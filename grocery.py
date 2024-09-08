n=[]
while True:
    try:
        m=input()
        n.append(m)
    except EOFError:
        break
n.sort()
print(f"{n.count(n[0])} {n[0].upper()}")
for i in range(1,len(n)):
    o=n.count(n[i])
    if n[i]!=n[i-1]:
        print(f"{o} {n[i].upper()}")
    else:
        continue

