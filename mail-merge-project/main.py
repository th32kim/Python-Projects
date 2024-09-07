PLACEHOLDER = "[name]"

with open("mail-merge-project/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
with open ("mail-merge-project/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"mail-merge-project/Output/ReadyToSend/{stripped_name}.txt", mode = 'w') as complete_letter:
            complete_letter.write(new_letter)

        
       

