from faces.twttr import shorten
def main():
  test_twttr()

def test_twttr():
  assert shorten("cs50")=="cs50"
  assert shorten("+91 9440371976")=="+91 9440371976"
  assert shorten("ManjunAtH")=="MnjntH"
  assert shorten("!@#$%^&*()_+")=="!@#$%^&*()_+"

if __name__ == "__main__":
    main()
