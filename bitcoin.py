import requests
import sys
import json
r=""

try:
  if len(sys.argv)<2:
    sys.exit("Missing command-line arguement")
  elif sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")
  elif sys.argv[1].isdigit() or float(sys.argv[1]):
    n=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o=n.json()
    p=o["bpi"]
    q=p["USD"]
    amount=q["rate"]
    for i in range(len(amount)):
      if amount[i]!=",":
        r=r+amount[i]
      else:
        pass
    print(f"${float(r)*float(sys.argv[1]):,.4f}")
except requests.RequestException:
  sys.exit()
