# mini project of calculator
first = int(input("enter the first number : "))
second = int(input("enter the second number : "))
oprator = input("enter operator (+,-,*,/,%) :")

if oprator == "+":
    print(first + second)
elif oprator == "-":
    print(first - second)
elif oprator == "*":
    print(first * second)
elif oprator == "/":
    print(first / second)
elif oprator == "%":
    print(first % second)
else:
    print("Oopps!!")