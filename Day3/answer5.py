# Reverse a Number
number = int(input("Enter a number: "))
reversed_number = 0
n=str(number)
for i in n:
    reversed_number=n[::-1]
print("Reversed number is:", reversed_number)

#alternative and easy version
# number = input("Enter a number: ")
#print("Reversed number is:", number[::-1])


