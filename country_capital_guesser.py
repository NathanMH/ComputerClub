#! /usr/bin/env python3

# This is called a python dictionary. It has keys (Canada, France etc...) and Valuse (Paris, Ottawa)
countries_capitals = {"Canada": "Ottawa", "United States": "Washington", "France": "Paris"}

# The variable "playing" determines if we will play the game. 1 = yes, 0 = no
playing = 1
correct_answers = 0
total_questions = 0
correct_percent = 0

while playing:
    for key, value in countries_capitals.items():
        answer = input("Name the capital of: " + key + "\n").lower()
        total_questions += 1 # Short for total_questions = total_questions + 1
        
        if answer == countries_capitals[key] or answer.title() == countries_capitals[key]:
            correct_answers += 1 
            print("Correct!")
        else:
            print("Wrong!")

    # Should we keep playing?
    response = input("Would you like to play again?: \n")
    if response.lower() == "no" or response == "n":
        playing = 0

correct_percent = (correct_answers / total_questions) * 100
print(str(round(correct_percent, 1)) + "%")
print("You scored " + str(correct_answers)+ "/" + str(total_questions))

#if correct_percent >= 80:
#    print(“:)”)


    
