num1=int(input("number1:"))
num2=int(input("number2:"))
small=min(num1,num2)
for i in range(1,small+1):
    if num1%i==0 and num2%i==0:
        com=i
print("gcd:",com)