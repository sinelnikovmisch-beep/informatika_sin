str = input("Enter word: ")
vowels = ['a', 'e', 'i', 'o', 'u']
cv = sum(map(lambda x: str.count(x), vowels))
print("Vowels: ", cv)
print("Consonants", len(str) - cv)
