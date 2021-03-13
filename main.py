#Step 1 
import random
import hangmanart
import hangmanwords
import replit

print(hangmanart.logo)
end_of_game = False
lives = 6

chosen_word = random.choice(hangmanwords.word_list)
print(chosen_word)

empty_array = []

for _ in chosen_word:
  empty_array.append("_")

while not end_of_game:
  guess = input("Guess a Letter from a - z? ").lower()
  replit.clear()
  if guess in empty_array:
    print(f"You've already guesses {guess}")

  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if guess == letter:
      empty_array[position] = letter
  print(f"{' '.join(empty_array)}")

  if guess not in chosen_word:
    lives -= 1 
    print(f"you guessed {guess}, Thats not in the word. you have {lives}'s lives remaining")
    
    
    if lives == 0:
      end_of_game = True
      print("You Lose")
      print(chosen_word)

  print(empty_array)

  if "_" not in empty_array:
    end_of_game = True
    print("You Won")

  print(hangmanart.stages[lives])
