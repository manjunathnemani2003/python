length=int(input("length: "))
list=[]

for i in range(length):
  n=int(input("nums: "))
  list.append(n)

def convert_to_binary(n):
  return bin(n[2:])

def check_condition(n1,n2):
  if (n1&n2)*2<(n1|n2):
    return True
  else:
    return False

count=0
print(list)
for i in range(len(list)-1):
  print(f"i value is {i}")
  if check_condition(list[i],list[i+1]):
    print(f"{list[i]} and {list[i+1]} satisfys condition")
    count=count+1

print(count)




