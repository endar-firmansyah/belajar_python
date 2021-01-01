# Python program to check if the input number is odd or even.
# A number is even if division by given 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number
# div = 79
div = int(input("Input a number: "))
if (div % 2) == 0:
    print("{0} is even Number".format(div))
else:
    print("{0} is Odd Number".format(div))

