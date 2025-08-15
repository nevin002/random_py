n=int(input("enter numbber:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
print("yes"if sum==n else "no")