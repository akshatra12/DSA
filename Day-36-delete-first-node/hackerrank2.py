def check_palindrome(word):
    left=0
    right=len(word)-1
    while left<right:
        if word[left]==word[right]:
            left+=1
            right-=1
        else:
            return "Not Palindrome"
    freq={}
    for i in word:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    count=0
    for key,value in freq.items():
        if value==1:
            count+=1
    return fact(count)

def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num* fact(num-1)
word = "level"
print(check_palindrome(list(word)))

