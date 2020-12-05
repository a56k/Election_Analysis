years = 80
list =()
list = ("for")
print("list")
# List Comprehension

 word = "Halibut"
 #push the letters in a array
 letters = []
 for letter in word:
     letters.append(letter)

#write as an expression
betterLetters = [letter for letter in word]
print(betterLetters)

# Rock Paper scissors

# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")
    print(computer_choice)
# Run Conditionals
if (user_choice == "r" and computer_choice == "r")
    print("Tie")

elif (user_choice == "r" and computer_choice == "S")
    print("You win")

