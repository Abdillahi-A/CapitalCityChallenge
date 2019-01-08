from continents import conts
import sys
import random
from fuzzywuzzy import fuzz

def leave_game():
    print("'\nThat's too bad. Come back when you want to play again.\nBye!")
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
    if fuzz.ratio(answer.lower(), city.lower()) != 100 and fuzz.ratio(answer.lower(), city.lower()) > 90:
        print(f"Hmmm I'll give you this one, but the correct spelling is {city}.\n")
        return True
    elif fuzz.ratio(answer.lower(), city.lower()) == 100:
        print("Well done! That is correct.\n")
        return True
    else:
        print("Sorry, the correct answer is {}\n".format(city))

def display_score(correct_answers, total_questions):
    print(f"You got {correct_answers} out of cities {total_questions} correct.")

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
    play_again = input("Do you want to play again? Please enter 'Y' or 'N'\n")
    
    while play_again.lower() not in ['y', 'n']:
        play_again = input("Please type 'Y' to continue or 'N' to quit\n")

    if play_again.lower() == 'y':
        return True
    
def main():
    print("Hey, Welcome to Capital City Challenge!\n")
    while True:  
        continent = choose_continent()
        continent = check_valid_continent(continent)
        print("Cool. You've Chosen {}. Let's see if you know your stuff.".format(continent.capitalize()))
        correct_answers, total_questions = ask_question(continent)
        score_the_game(correct_answers, total_questions)
        if not play_again():
            leave_game()
            break
            
main()
