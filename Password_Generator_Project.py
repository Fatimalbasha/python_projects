import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the Password Generator!")
print("Would you like your password to be ordered (letters first, then symbols, then numbers)?")
print("Or would you prefer it to be randomized for better security?")


while True:
    try:
        user_choice = int(input("Enter 1 for an ordered password, or 2 for a randomized (more secure) password: "))
        if user_choice == 1 or user_choice == 2:
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Please enter a numeric value (1 or 2).")
            


nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password_list = []

for i in range(nr_letters):
    password_list.append(random.choice(letters))

for i in range(nr_symbols):
    password_list.append(random.choice(symbols))

for i in range(nr_numbers):
    password_list.append(random.choice(numbers))


if user_choice == 1: 
    #Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    password_ordered = "".join(password_list)
    print("Your new password (ordered) is: ", password_ordered )

elif user_choice == 2:
    #Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    random.shuffle(password_list)
    password_not_ordered = "".join(password_list)
    print("Your new password (randomized) is: ", password_not_ordered )









