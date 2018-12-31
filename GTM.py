# "Guess the number" mini-project
# http://www.codeskulptor.org/#user40_pnN71lvBlH_3.py

# import libraries
import math
import random
import simplegui

# helper function to start and restart the game

def new_game():
    # initialize global variables used in your code here
    global guess
    global secret_number
    global max_guess
    global guess_inc
    max_guess = 7
    guess = 0
    guess_inc = 0
    secret_number = random.randrange(0, 100)
        
# define event handlers for control panel

    # button that changes the range to [0,100) and starts a new game 
def range100():
    global secret_number
    global max_guess
    new_game()
    max_guess = 7
    secret_number = random.randrange(0, 100) 

    # button that changes the range to [0,1000) and starts a new game   
def range1000():
    global secret_number
    global max_guess
    new_game()
    max_guess = 10
    secret_number = random.randrange(0, 1000) 
    
def input_guess(g):
    global guess
    global secret_number
    global max_guess
    global guess_inc
    int_guess = int(g)
    print "Guess was", int_guess
    # main game logic
    if int_guess < secret_number:
        print "Higher"
    elif int_guess > secret_number:
        print "Lower"
    elif int_guess == secret_number:
        print "Correct" 
    guess_inc = guess_inc + 1
    print "Have guessed", guess_inc,"time(s)."
    if guess_inc >= max_guess:
        print "Sorry. Out of guesses."
        new_game()
       
# create frame
f = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
f.add_button("Start new game",new_game,200)
f.add_button("Range 0 to 100",range100,200)
f.add_button("Range 0 to 1000",range1000,200)
f.add_input("Input guess",input_guess,200)

# get frame rolling
f.start()

# call new_game 
new_game()




