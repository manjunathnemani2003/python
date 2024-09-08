# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
nums=[1,3,2]
n=0
a=[]
for i in range(1,len(nums)):
    if nums[-i]>nums[-i-1]:
        # nums[-i],nums[-i-1]=nums[-i-1],nums[-i]
        n=nums.index(nums[-i])
        break
if n!=0:
    for i in range(1,(len(nums)-n)):
        a.append(nums[-i])
        nums.pop()
    a.sort()
    for i in range(len(a)):
        if nums[n-1]<a[i]:
            nums[n-1],a[i]=a[i],nums[n-1]
            break
    a.sort()
    for i in a:
        nums.append(i)
else:
    if n==0:
        nums.sort()
print(nums,a,n)
