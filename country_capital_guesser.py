#! /usr/bin/env python3

#######################
"""####################
Index:
    1. Imports and Readme
    2. Functions
    3. Main
    4. Testing
####################"""
#######################

###################################################################
# 1. IMPORTS AND README
###################################################################

import easygui
import country_list_getter

###################################################################
# 2. FUNCTIONS
###################################################################

# Dictionary. It has keys (Canada, France etc...) and Values (Paris, Ottawa)
country_list_getter.main()
COUNTRIES_CAPITALS = country_list_getter.final_list

def ask_to_play():
    return easygui.ynbox("Do you want to play a game?", "Country Guesser", ("Yes", "No"))

def ask_to_replay(correct_answers, total_questions):
    score = round(((correct_answers / total_questions) * 100), 2)
    if score >= 50:
        return easygui.buttonbox("Your score: " + str(score) + ". Do you want to play again?", "~/Documents/ComputerClub/assets/happy_puppy.jpg", ["Yes", "No"])
    else:
        return easygui.buttonbox("Your score: " + str(score) + ". Do you want to play again?", "~/Documents/ComputerClub/assets/sad_puppy.jpg", ["Yes", "No"])

def main_question_box(country):
    return easygui.enterbox("What is the capital of: " + country + "?", "Country Capital Guesser!!")


###################################################################
# 3. MAIN
###################################################################

def funtime():
    playing = 1
    correct_answers = 0
    total_questions = 0
    ask_to_play()
    while playing:
        for key, value in COUNTRIES_CAPITALS.items():
            answer = main_question_box(key)
            # answer = input("Name the capital of: " + key + "\n").lower()
            total_questions += 1 # Short for total_questions = total_questions + 1

            if answer == COUNTRIES_CAPITALS[key] or answer.title() == COUNTRIES_CAPITALS[key]:
                correct_answers += 1
                print("Correct!")
            else:
                print("Wrong!")

        # Should we keep playing?
        response = input("Would you like to play again?: \n")
        if response.lower() == "yes" or response == "y":
            playing = 1
        else:
            playing = 0

    #score_screen(correct_answers, total_questions)
    ask_to_replay(correct_answers, total_questions)
    #print("You scored " + str(correct_answers)+ "/" + str(total_questions) + " (" + str(correct_percent) + "%)")


###################################################################
# 4. TESTING
###################################################################

# COUNTRIES_CAPITALS = {"Canada": "Ottawa", "United States": "Washington", "France": "Paris"}

def test_1():
    pass
# ask_to_play()
# main_question_box("Canada")

funtime()
