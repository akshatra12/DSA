# Palindrome
def check_palindrome(word):
    left=0
    right=len(word)-1
    while left<right:
        if word[left]==word[right]:
            left+=1
            right-=1
        else:
            return False
    return True
word="madam"
print(check_palindrome(word))