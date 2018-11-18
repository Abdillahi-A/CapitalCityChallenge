from continents import conts
import sys
import random
from fuzzywuzzy import fuzz


    
def check_valid_response():
    wants_to_play = input()
    while wants_to_play.lower() not in ['yes', 'no']:
        wants_to_play = input("Sorry that is not a valid option. Please choose 'yes' or 'no'\n")
    return wants_to_play


def leave_game(wants_to_play):
    print("'\nThat's too bad. Come back when you are ready to play.'")
    print('\nBye!')
    sys.exit()


def choose_continent():
        continent = input("Choose a continent: \n{}\n\n".format('\n'.join(conts)))
        return continent
        
    
def check_valid_continent(continent):
    while continent.capitalize() not in conts.keys():
        continent = input("Sorry that is not a valid response. Please choose one of the follwoing continents: \n{}\n\n".format('\n'.join(conts.keys())))
        
    return continent
    
def randomise_countries(continent):
    items = list(conts[continent.capitalize()].items())
    random.shuffle(items)
    return items

def ask_question(continent):
    correct_answers = 0
    total_questions = len(conts[continent.capitalize()])
    items = randomise_countries(continent)
       
    for country,city in items:
        answer = input('What is the capital city of {}\n'.format(str(country)))
        if check_answer(answer, city) == True:
            correct_answers += 1
    
    return correct_answers, total_questions
        
        
def check_answer(answer, city):
    if answer.lower() == 'quit':
        wants_to_play = 'no'
        leave_game(wants_to_play)
    elif fuzz.ratio(answer.lower(), city.lower()) > 90:
        print("Well done! That is correct.")
        return True
    else:
        print("Sorry, the correct answer is {}".format(city))

def display_score(correct_answers, total_questions):
    print(f"You got {correct_answers} out of cities {total_questions} correct.")

'''def show_results(total_questions, correct_answers):
    print("Results:\n You got {}/{} correct.".format(correct_answers,total_questions))'''

def score_the_game(correct_answers, total_questions):
    print('\nResult:')
    if correct_answers / total_questions == 1:
        display_score(correct_answers, total_questions)
        print('Wow, you really know your stuff. Very Impressed!')
    elif correct_answers / total_questions > 0.7:
        display_score(correct_answers, total_questions)
        print('Quite the geographer we have here. I am impressed')
    elif correct_answers / total_questions > 0.5:
        display_score(correct_answers, total_questions)
        print('Not bad, not bad at all.')
    elif correct_answers / total_questions > 0.4:
        display_score(correct_answers, total_questions)
        print('Admirable attemp young Grasshopper. Though there is yet room for improvement.')
    else:
        display_score(correct_answers, total_questions)
        print('Looks like you need a little more practice.') 

def play_again():
    wants_to_play = input("Do you want to play again? Please enter 'Yes' or 'No'\n")
    
    while wants_to_play.lower() not in ['yes', 'no']:
        wants_to_play = input("Please type 'yes' or 'no'\n")
    
    return wants_to_play
    

    
def main():
    print("Hey!\nWelcome to Capital City Challenge!\nAre you ready to play? Yes or No")
    wants_to_play = check_valid_response()
    if wants_to_play.lower() == 'no':
        leave_game(wants_to_play)
        
    while wants_to_play.lower() == 'yes':
        print("\nCool let's play!")
        continent = choose_continent()
        continent = check_valid_continent(continent)
        print("Cool. You've Chosen {}. Let's see if you know your stuff.".format(continent.capitalize()))
        print("Psss type 'quit' if you get bored and wat to exit game.\n")
        correct_answers, total_questions = ask_question(continent)
        score_the_game(correct_answers, total_questions)
        wants_to_play = play_again()
    else:
        leave_game(wants_to_play)
        
main()