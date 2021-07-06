# First we get a print that we have welcomed
print("welcome the number gusses")
# We create a function that you will find out later why
# We use the random function for different numbers
def number ():
    import random
# Here we use the random function, we say give different numbers from one to the desired number
    number = random.randint(1, 50)
# Here, too, we ask the name of the other party
    player_name = input("Hello, What's your name?")
# Then here we give number_og_gusses zero until we say how many times we guessed
    number_of_guesses = 0
# Here, too, we say whatever we want to our liking, then we say, guess the desired user from one to the number you want.
    print('okay!  {}  I am Guessing a number between 1 and 50:'.format(player_name))

# Here we define a loop, divide the desired number by 2, and then say the desired number was smaller, say low was larger, say high, and so on.
    while number_of_guesses <= 25:
        guess = int(input())
        number_of_guesses += 1

        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            print("you wine very good")
        # here too break
            break
# Here, too, I said above, we give it zero. Now, we made it one by one, then we put it in print to say how many times we guessed and it was correct.
    if guess == number:
            print('You guessed the number in {} tries!'.format(number_of_guesses))
# Here we write in the circle, if it was not correct, say this was the desired number
    else:
            print('You did not guess the number, The number was  {}'.format(number))

# And here, like the previous code, we ask the question that it wants to guess the number again
    again()

def again():

    gusses_again = input('''
    Do you want to gusses again?
    Please type Y for YES or N for NO.
    ''')
    if gusses_again.upper() == 'Y':
        number ()
    elif gusses_again.upper() == 'N':
        print('See you later.')
    else:
        again()
number()
# output : >>
# welcome the number gusses
# Hello, What's your name?mohamad
# okay!  mohamad  I am Guessing a number between 1 and 50:
# 21
# Your guess is too high
# 20
# Your guess is too high
# 12
# Your guess is too high
# 10
# Your guess is too low
# 11
# you wine very good
# You guessed the number in 5 tries!

#     Do you want to gusses again?
#     Please type Y for YES or N for NO.
#     n
# See you later.