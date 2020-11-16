"""Simply Calculator program"""

# Addition function code
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multifly(a, b):
    return a * b

def divide (a, b):
    return a / b

print ("Choose Options")
print ("1. Addition")
print ("2. Substraction") 
print ("3. Multiplication")
print ("4. Division")

choice = input("Choose Options (1 or 2 or 3 or 4): ")

num1 = int(input("Type first number: "))
num2 = int(input("Type second number: "))

if choice == "1":
    print(num1,"+",num2,"=", add(num1,num2))

if choice == "2":
    print(num1,"-",num2,"=", subtract(num1,num2))

if choice == "3":
    print(num1,"*",num2,"=", multifly(num1,num2))

if choice == "4":
    print(num1,"/",num2,"=", divide(num1,num2))
"""else:
    print("Wrong input")"""



