#Python3 program to find factorial of given number

def Factorial(n): 
  
    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * Factorial(n - 1)  
    
    # Driver Code 
num = int(input("Enter the number: "))
print ("Factorial of",num,"is", 
      Factorial(num)) 
  
# This code is contributed 
# by Smitha Dinesh Semwal. 