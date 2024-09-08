class Jar:
    extraadd=0       # mistaken use of a class variable

    def __init__(self, c):
        if int(c)<0:
            raise ValueError("negative no of cookies")
        self.c = c

    def add(self, extra):
        if self.extraadd+extra>int(self.c):
            raise ValueError("too many cookies")
        else:
            self.extraadd=self.extraadd+extra

    def sub(self, extra):
        if self.extraadd-extra<0:
            raise ValueError("ran out of cookies")
        else:
            self.extraadd=self.extraadd-extra

    @property
    def capacity(self):
        return self.c

    @property
    def size(self):
        return self.extraadd

    def __str__(self):
        s=""
        for i in range(int(self.c)):
            s=s+"@"
        return s

n=input("enter the capacity of jar: ")
d=Jar(n)
d.add(4)
d.sub(4)
print(f"capacity of the jar: {d.capacity}")
print(f"current size of jar: {d.size}")

