n = int(input("Enter the number: "))
print("The first N odd natural numbers: ")
for i in range(n,1,-1):
    if i%2!=0:
        print(i,end=" ")