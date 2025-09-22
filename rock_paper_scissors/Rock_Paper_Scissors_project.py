import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''  

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

print("For a Rock Paper Scissors game against the computer")

try: 
    player_choise = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors: "))
    if player_choise < 0 or player_choise > 2:
        print("You typed an invalid number")

    else:
            computer_choise = random.randint(0, 2)

            print("Computer chose: ")
            print(game_image[computer_choise])
            
            print("Your chose: ")
            print(game_image[player_choise])


            if player_choise == 0 and computer_choise == 2:
                print("You win!  ^‿^ ") 

            elif player_choise == 2 and computer_choise == 0:
                print("You lose!")

            elif player_choise < computer_choise:
                print("You lose!") 

            elif player_choise > computer_choise:
                print("You win!  ^‿^ ")

            elif player_choise == computer_choise:
                print("It's a draw!")

            print()
        
except ValueError:
    print("Invalid input! Please enter a whole number like 0, 1, or 2")

