s='11 10 6'
c=0
for i in range(len(s)-1):
  if s[i]=='0' and (s[i+1] in '123456789'):
    c=c-2
  elif s[i]=='2' and (s[i+1] in '0123456'):
    c=c+1
  elif s[i]!='0' and (s[i+1] in '123456789'):
    c=c+2

print(c)

