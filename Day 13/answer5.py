# Reverse String Using Two Pointers
def reverse_string(word):
    left=0
    right=len(word)-1
    while left<right:
        word[left],word[right]=word[right],word[left]
        left+=1
        right-=1
    return word
word=input("Enter a string: ")
reverse=reverse_string(list(word))
print(''.join(reverse))
# reversed_word=reverse_string(list(word))
# print("Reversed string: ", ''.join(reversed_word))
