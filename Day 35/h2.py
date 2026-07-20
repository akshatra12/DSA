#h2 
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
    for key,value in freq.items(): 
        if value==1: 
            return key 
    return "No Unique Character" 
word = "madam" 
print(check_palindrome(list(word)))