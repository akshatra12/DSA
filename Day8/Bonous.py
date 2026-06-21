# find the palindrome of a string and reverse the string without using built in functions.
word = input("Enter a string: ")

reverse = ""

for i in range(len(word)-1, -1, -1):
    reverse += word[i]

print(reverse)

# Check if the string is a palindrome
if word == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")