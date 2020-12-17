# Python program to find maximum of two numbers
print("This is program to find max number")
def maxnumber(w, x, y, z):
	if w >= x:
		return w
	elif x >= y:
		return x
	elif y >= z:
		return y
	else:
		return z

# Input number by user, we can use integer or float
w = float(input("Please input the first number: "))
x = float(input("Please input the second number: "))
y = float(input("Please input the third number: "))
z = float(input("Please input the third number: "))

print("The Max number is", maxnumber(w, x, y, z))

