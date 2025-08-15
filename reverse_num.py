nu=int(input("Enter number to reverse:"))
n=str(nu)
sum=0
while nu>0:
    rem=nu%10
    sum=sum*10+rem
    nu=nu//10
print(sum)  
    