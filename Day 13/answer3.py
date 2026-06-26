def check_palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            return False
    return True
word=input("Enter a word: ")
if check_palindrome(word):
    print(True)
else:
    print(False)