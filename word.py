# In the first step, we have to give the computer 
# a list from which to choose the word show. There are many ways to do this. 
# I did this by defining a list and selecting one with a random module.
import random
name = input("What is your name? ")
print ("Hello, {} Time to play hangman!".format(name))
print ("Start guessing...\n")
# I also want to give the user five chances to guess that with each wrong 
# letter one of the chances decreases and when the game reaches zero, the game is over.
words = ['python','php','swif','katolin','matlab' , 'java' , 'javascrip']
# The next thing is that the user did not make any guesses at the beginning
#  of the game, so her guess is empty and is added to it during the game.
print(words)
# There are two things that need to be done in this section.
#  One is to show us the number of letters. Second, for each correct letter
#  that the user guessed, remember to display the letter, 
# otherwise leave a space.
word = random.choice(words)
guesses = ''
turns = 5
# Let's see what happens if the player guesses wrong
# . Suffice it to say that if his guess is wrong,
#  one of his chances will be lost
while turns > 0:         
    failed = 0             
    for char in word:
# In this section, we also want to see if the user has won or not?
#  If his chance is over, the game is over.
        if char in guesses:    
            print (char,end=(""))    
        else:
            print ("",end=""),     
            failed += 1    
    if failed == 0:        
        print (' You won' ) 
        break              
    guess = input("\n \n  guess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("\n  Wrong")    
        print('\n You have {} more guesses'.format(turns)) 
        if turns == 0:           
            print ("\nYou Lose") 
