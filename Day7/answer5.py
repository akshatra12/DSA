# Count Vowels
word="programming"

vowel=["a","e","i","o","u"]

count=0

for char in word:
    if char in vowel:
        count+=1

print(count)