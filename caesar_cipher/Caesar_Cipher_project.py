import ceasar_cipher_art

print(ceasar_cipher_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else: 
            letter_in_list = alphabet.index(letter)
            shifted_position = letter_in_list + shift_amount
            encrypted_letter = alphabet[(shifted_position) % len(alphabet) ]
            output_text += encrypted_letter
                
    return f"Here is the {encode_or_decode}d result: {output_text}"


should_continue = True

while should_continue: 
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in ["encode", "decode"]:
            break
        else:
            print("Invalid input. Please type 'encode' or 'decode'.")
    
    text = input("Type your message:\n").lower()


    while True:
         try:
            shift = int(input("Type the shift number:\n"))
            break
         except ValueError:
              print("Invalid number. Please enter an integer")
        
    print(caesar(text, shift, direction))


    while True:
        restart = input("Type 'yes' if you want to go again. otherwise type 'no': \n").lower()
        if restart in ["no","yes"]:
            break
        else: 
            print("Invalid input. Please type 'yes' or 'no'.")
    if restart == 'no':
        should_continue = False
        print("Hope you had fun encoding and decoding!🔐")

