from faces.um import count
def main():
  print(test_um1())
  print(test_um2())
  print(test_um3())

def test_um1():
  assert count("Um?")==1

def test_um2():
  assert count("yummy gum")==0
  assert count("hi, um..whats ur name")==1

def test_um3():
  assert count("Um! thanks um..mum")==2

if __name__ == "__main__":
    main()
