from faces.bank import value
def main():
  test_value1()
  test_value2()
  test_value3()

def test_value1():
  assert value("Hello, newman")=="$0"
  assert value("ho?")=="$20"

def test_value2():
  assert value("!@#$%^&*()_+")=="$100"
  assert value("hH")=="$20"

def test_value3():
   assert value(" ")=="$100"
   assert value("hello")=="$0"


if __name__ == "__main__":
    main()

