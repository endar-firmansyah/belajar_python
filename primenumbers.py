# Python program to print all prime numbers

start = input("Enter the start number: ")
end = input("Enter the end number: ")

for i in range(start,end):
    if i>1:
        for j in range(2,i):
            if(i % j==0):
                break

        else:
            print(i)