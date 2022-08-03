print("Enter marks of oops: ")
a=int(input())
print("Enter marks of dsu: ")
b=int(input())
print("Enter marks of java: ")
c=int(input())
print("Enter marks of python: ")
d=int(input())
print("Enter marks of C: ")
e=int(input())
total=a+b+c+d+e
print("Total marks: ",total)
if total>=75:
    print("Distinction")
elif total>=60:
    print("A Grade")
elif total>=50:
    print("B Grade")
elif total>=40:
    print("C Grade")
else:
    print("Fail")
