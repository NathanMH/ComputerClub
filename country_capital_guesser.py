#! /usr/bin/env python3

import easygui

# This is called a python dictionary. It has keys (Canada, France etc...) and Values (Paris, Ottawa)
countries_capitals = {"Canada": "Ottawa", "United States": "Washington", "France": "Paris"}

def ask_to_play(results):
    return easygui.ynbox("Do you want to play a game?", "Country Guesser", ("Yes", "No"))

def main_question_box(country):
    return easygui.enterbox("What is the capital of: " + country + "?", "Country Capital Guesser!!")

def score_screen(correct_answers, total_questions):
    correct_percent = round(((correct_answers / total_questions) * 100), 2)
    if correct_percent >= 80:
        #ask_to_play()
        print(":D")
    elif correct_percent >= 60:
        print(":)")
    elif correct_percent >= 40:
        print(":(")
    else:
        print(":'(")

###############################################
# Main
###############################################

def funtime():
    playing = 1
    correct_answers = 0
    total_questions = 0
    correct_percent = 0
    ask_to_play()
    while playing:
        for key, value in countries_capitals.items():
            answer = main_question_box(key)
            # answer = input("Name the capital of: " + key + "\n").lower()
            total_questions += 1 # Short for total_questions = total_questions + 1

            if answer == countries_capitals[key] or answer.title() == countries_capitals[key]:
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

    score_screen(correct_answers, total_questions)
    print("You scored " + str(correct_answers)+ "/" + str(total_questions) + " (" + str(correct_percent) + "%)")

###############################################
# Testing
###############################################

def test_1():
    pass
# ask_to_play()
# main_question_box("Canada")
    
funtime()
