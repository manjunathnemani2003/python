from faces.numb3rs import validate
def main():
  test_num1()
  test_num2()
  test_num3()

def test_num1():
  assert validate("cs50")==False
  assert validate("0.0.0.0")==True
  assert validate("255.0.0.0")==True
  assert validate("1.1000.1000.1000")==False

def test_num2():
  assert validate("+91 9440371976")==False
  assert validate("255.255.255.255")==True

def test_num3():
  assert validate("ManjunAtH")==False
  assert validate("!@.#$.%^&.*()._+")==False
  assert validate("512.512.512.512")==False
  assert validate("127.0.0.1")==True
  assert validate("127.0.0.10000")==False


if __name__ == "__main__":
    main()
