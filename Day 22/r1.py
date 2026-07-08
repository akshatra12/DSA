
def rev_vowel(word):
    vowel="aeiouAEIOU"
    left=0
    right=len(word)-1
    while left<right:
        if word[right] in vowel and word[left] in vowel:
            word[left],word[right]=word[right],word[left]
            left+=1
            right-=1
        elif word[right] not in vowel:
            right-=1
        elif word[left] not in vowel :
            left+=1
        else:
            left+=1
            right-=1
    return word

word = "programming"
result=rev_vowel(list(word))
print("".join(result))
