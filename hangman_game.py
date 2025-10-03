import random
import hangman_stages

word_list = ["apple","brownie","potato","rocket","flower"]
chance = 6
chosen_word = random.choice(word_list)

print("🎮 Welcome to Hangman!")

display = []
for i in range (len(chosen_word)):
    display += '_'
print(display)

game_over = False
while not game_over:
    
    guessed_letter = input("Guess the letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    print(display)

    if guessed_letter not in chosen_word:
        chance -= 1
        if chance == 0:
            game_over = True
            print("you lose💀!!")

    if "_" not in display:
        game_over = True
        print("🎉 Congratulations! You won! 🎉")
    print(hangman_stages.stages[chance])

print("\n🎯 Thanks for playing Hangman!")
