arr=[1,10,30,90,100,150,370,520,1000,1001,1002,1003,1200]
num=int(input("number: "))
c=[6]
mid=int((len(arr)-1)/2)
first=0
last=len(arr)-1

def search(f,l,mid,c):
  c.append(mid)
  if len(c)>2:
    if c[-2]==c[-1]:
      print('not found')
      return 1
  if num==arr[mid]:
    print('found',mid)
  elif num<arr[mid]:
    search(f,mid-1,int((f+mid-1)/2),c)
  else:
    search(mid+1,l,int((mid+1+l)/2),c)

search(first,last,mid,c)



