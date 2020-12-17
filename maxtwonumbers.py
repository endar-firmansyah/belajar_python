# Python program to find maximum of two numbers
print("This is program to find max number")
def maxnumber(x, y, z):
	if x >= y:
		return x
	elif y >= z:
		return y
	else:
		return z

# Input number by user, we can use integer or float
x = float(input("Please input the first number: "))
y = float(input("Please input the second number: "))
z = float(input("Please input the third number: "))

print("The Max number is", maxnumber(x, y, z))
