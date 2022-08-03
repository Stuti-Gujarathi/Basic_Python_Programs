print("Enter the value of first number: ")
x=int(input())
print("Enter the value of second number: ")
y=int(input())
print("Enter the value of third number: ")
z=int(input())
if (x>y) and (x>z):
    print("First number is greater")
elif (y>x) and (y>z):
    print("Second number is greater")
else:
    print("Third number is greater")
