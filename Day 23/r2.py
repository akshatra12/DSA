#R2 Reverse Vowels + Palindrome
def check_palindrome(word):
    vowel="aeiouAEIOU"
    left=0
    right=len(word)-1
    while left<right:
        if word[left] in vowel and word[right] in vowel:
            word[left],word[right]=word[right],word[left]
            left+=1
            right-=1
        elif word[left] not in vowel:
            left+=1
        elif word[right] not in vowel:
            right-=1
        else:
            left+=1
            right-=1
    return word==word[::-1]
word = "aebcbda"
print(check_palindrome(list(word)))
