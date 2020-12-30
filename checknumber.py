#Pythhon program to check if the input numbers is (Positive, Negative, Zero)
num = int(input("Enter a Number: "))
if num > 0:
    print("{0} is Positive Number".format (num))
elif num == 0:
    print("{0} is Zero".format (num))
else:
    print("is Negative Number")

