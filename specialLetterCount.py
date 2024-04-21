def count_special_letters(word):
  special_letters = set()
  
  for char in word:
    if char.lower() != char.upper and char.lower() in word and char.upper() in word:
      special_letters.add(char.lower())

  return len(special_letters)

print(count_special_letters("aaAbcBC"))  # Output: 3
print(count_special_letters("abc"))      # Output: 0
print(count_special_letters("abBCab"))   # Output: 1
