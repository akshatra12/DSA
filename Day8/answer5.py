# Count Vowels and Consonants
word = "programming"

vowel=["a","e","i","o","u"]

vowels=0
consonants=0

for char in word:
    if char in vowel:
        vowels+=1
    else:
        consonants+=1

print(f"vowels = {vowels}")
print(f"consonants = {consonants}")