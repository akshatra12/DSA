# Find largest of three numbers

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if a>b and a>c:
    print(a,"is larger")
elif c>a and c>b:
    print(c ,"is larger")
else:
    print(b, " is larger")