from continents import continents
import sys
import random


def welcome_message():
    print('Hey!\nWelcome to Capital City Challenge!')
    print('Are you ready to play? Yes or No')

def user_selects_valid_continent(continent):
    return continent.lower() in continents.keys()

def check_answer(continent, answer, city, country):
    total = len(continents[continent])
    correct = 0
    
    if answer.lower() == 'quit':
        print("Are you sure you want to quit? Enter 'Yes' to exit game")
        quit_mid_game = input()
        if quit_mid_game.lower() == 'yes':
            play = 'NO'
            leave_game(play) 
    elif answer.lower() == city.lower():
        correct += 1
        print('Well Done! That is correct.')
        print('\n')
    else:
        print('Sorry,that is incorrect. The capital city of ' + str(country) + ' is ' + str(city))
        print('\n')
            
    return correct, total

def randomise_countries(continent):
    items = list(continents[continent].items())
    random.shuffle(items)
    return items
    

def ask_questions(continent):
    items = randomise_countries(continent)
    for country, city in items:
        print('What is the capital of ' + str(country))
        answer = input()
        correct, total = check_answer(continent, answer, city, country)
    
    return correct, total
        

def play_the_game():
    print("Cool let's play!\n\nPlease choose a Continent:\nAfrica \nAsia \nEurope \nAmericas \nOceania")
    continent = input()
    while not user_selects_valid_continent(continent):
        print('\nI\'m sorry that is not a valid option. Please choose one of the following Continents:\nAfrica \nAsia \nEurope \nAmericas \nOceania')
        continent = input()

    if user_selects_valid_continent(continent):
        print('Ok let\'s see if you know your stuff.')
        print("Psssss if you want to quit. Just type 'quit' and the game will exit.\n")
        
    return continent
 
    
def display_score(correct, total):
    print(f"You got {correct} out of cities {total} correct.")
    

def score_the_game(correct, total):
    print('Result:')
    if correct / total == 1:
        display_score(correct, total)
        print('Wow, you really know your stuff. Very Impressed!')
    elif correct / total > 0.7:
        display_score(correct, total)
        print('Quite the geographer we have here. I am impressed')
    elif correct / total > 0.5:
        display_score(correct, total)
        print('Not bad, not bad at all.')
    elif correct / total > 0.4:
        display_score(correct, total)
        print('Admirable attemp young Grasshopper. Though there is yet room for improvement.')
    else:
        display_score(correct, total)
        print('Looks like you need a little more practice.')  
        
    
def check_user_input_valid_response():
    play = input()
    while play.lower() not in ['yes', 'no']:
    	print('Are you ready to play? Please type yes or no')
    	play = input()
    
    return play

def leave_game(play):
    print("That's too bad. Come back when you are ready to play.")
    print('Bye!')
    sys.exit()

def play_again():
    print("\nDo you want to play again?")
    play = str(input())
    while play.lower() not in ['yes', 'no']:
        print("Type 'Yes' to play again. Or type 'No' to exit game.")
        play = str(input())
    return play.upper()
    
    

def main():
    welcome_message()
    play = check_user_input_valid_response()
    
    if play.upper() == 'NO':
        leave_game(play)
    
    while play.upper() == 'YES':
        continent = play_the_game()
        correct, total = ask_questions(continent)
        score_the_game(correct, total)
        play = play_again()
    else:
        leave_game(play)
        
if __name__ == "__main__":
    main()
  

