import validators

a=input("enter email: ")
if validators.email(a):
  print("valid")
else:
  print("invalid")
