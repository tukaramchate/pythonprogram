num1 = int(input("enter the number 1 : "))
num2 = int(input("enter the number 2 : "))
num3 = int(input("enter the number 3 : "))

if num1 > num2 and num1 > num3:
    print("num1 is greatest")
elif num2 > num3 and num2 > num3:
    print("num2 is greatest ")    
else:
    print("num3 is greatest")