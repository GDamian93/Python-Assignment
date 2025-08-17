#Basic Calculator
#This program create a basic Calculator that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division) and print the result.
num1 = int(input("Enter with first number: "))
operator = input("Choose de operator  (+) (-) (*) (/): ")
num2 = int(input("Enter with secand number: "))

if operator == "+":
    result = num1 + num2    
elif operator == "-":
    result = num1 - num2    
elif operator == "*":
    result = num1 * num2    
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = None
if result is not None:
    print(f"{num1} {operator} {num2} = {result}")
else:
    print("INVALID OPERATION, DIVISON BY ZERO!!!") 
