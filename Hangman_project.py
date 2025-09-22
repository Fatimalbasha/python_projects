import random
import hangman_art
import hangman_words

lives = 6

print(hangman_art.logo + '\n')

chosen_word = random.choice(hangman_words.word_list)
#print(chosen_word)

place_holder = ""
for position in range(len(chosen_word)):
    place_holder += "_"
print("Word to guess: " + place_holder + '\n')

game_over = False
correct_letters = []

while not game_over: 
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input('\n' + "Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed: {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else: 
            display += "_"
    
    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1 
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True  
            print("\n" + f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])

