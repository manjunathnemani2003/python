nums = [1,3,6,7,9,4,10,5,6]
d=1
c=[]
gm=0
for i in range(len(nums)):
  c.append(nums[i])
  for j in range(i+1,len(nums)):
    if nums[j]>c[-1]:
      c.append(nums[j])
      d=d+1
    if nums[j]<c[-1] and nums[j]>nums[i]:
      c[-1]=nums[j]
    print(nums[j],c)
    print(f'd is {d}')
  if d>gm:
    gm=d
  d=1
  c=[]
print(gm)
