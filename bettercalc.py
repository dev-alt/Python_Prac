num1 = float(input("Enter first number: "))
opt = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if opt == "+":
    print(num1 + num2)
elif opt == "-":
    print(num1 - num2)
elif opt == "*":
    print(num1 * num2)
elif opt =="/":
    print(num1 / num2)   
else:
    print("Invalid")         


