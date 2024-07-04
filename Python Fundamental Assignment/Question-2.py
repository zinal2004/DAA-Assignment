N = int(input("N numbers are: "))
if N<0:
    print("Give a positive number")
else:
    sum = N*(N+1)//2
    print (f"sum of first {N} numbers is {sum}.")
