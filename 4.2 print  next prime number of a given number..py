n = int(input("Enter the number: "))
print("The next prime of {}: ".format(n))
while(n>1):
    n=n+1
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)
            break