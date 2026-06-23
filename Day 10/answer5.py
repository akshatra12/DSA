# Count Vowels
def count_vowels(word):
    vowels="aeiouAEIOU"
    count=0
    for i in word:
     if i in vowels:
        count+=1
    return count

if __name__ == "__main__":
    word=input("Enter a word: ")
    print(f"The number of vowels in the word '{word}' is: {count_vowels(word)}")