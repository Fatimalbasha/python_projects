def calculate_love_score(name1, name2):
    names_compine = name1.lower() + name2.lower()

    true_count = 0
    for char in names_compine:
        if char in 'true':
            true_count += 1
     
    
    love_count = 0
    for char in names_compine:
        if char in 'love':
            love_count += 1

    love_score = str(true_count) + str(love_count)

    return(love_score)



print("💖 Welcom to Love Calculator 💖")
print("Let's see how compatible your names are based on the magic of 'TRUE LOVE'!")
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
output = calculate_love_score(name1, name2)
print(output)
