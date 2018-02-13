#Write a Python program to reverse a word after accepting the input from the user.

yourWord = input("Please enter your word: ")

for char in range(len(yourWord) - 1, -1, -1):
  print(yourWord[char], end="")
print("\n")