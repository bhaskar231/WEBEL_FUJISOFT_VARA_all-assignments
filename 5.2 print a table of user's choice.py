n=int(input("Enter the number to to print table: "))
for i in range(1,11):
    mul=n*i
    print("{0} x {1}=".format(n,i),end=" ")
    print(mul)