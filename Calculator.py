  #Taking input from users
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
operator = input("enter operator (+, -, *, /): ") 
#Using if/else condition 
if operator == "+":
    result = num1 + num2
    print("Result is:", result)
elif operator == "-":
    result = num1 - num2
    print("Result is:", result)
elif operator == "*":
    result = num1 * num2
    print("Result is:", result)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Division by zero not allowed")
else:
    print("Enter valid operator (+, -, *, /)")

