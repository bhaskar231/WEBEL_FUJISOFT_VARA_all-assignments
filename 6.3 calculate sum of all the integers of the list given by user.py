l=[]
n=int(input("Enter the number of element: "))
for i in range(0,n):
    m=int(input())
    l.append(m)
sum=0
for j in l:
    sum=sum+j
print("the sum: ",sum)