numRows=int(input(""))
n=[1,[1,1]]
m=[]
if numRows==1:
  n=[[1]]
elif numRows==2:
  n=[[1],[1,1]]
else:
  for i in range(3,numRows+1):
    m.append(1)
    for j in range(1,i-1):
      m.append(n[-1][j-1]+n[-1][j])
    m.append(1)
    n.append(m)
    m=[]
print(n)
