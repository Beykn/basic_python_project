import random

randomnum=random.randrange(1,50)
guesscount = 6
try:
    while(guesscount != 0):
        number=int(input('Enter a number between 1-50 : '))
        if number == randomnum:
            print('Congratulations!')
            break
        elif number > randomnum:
            print('Try Again! You guessed higher than random number')
        else:
            print('Try Again! You guessed lower than random number')
        guesscount -= 1

    if guesscount == 0:
        print('Your guess is over')
except (ValueError, TypeError ) as msg:
    print(msg)
except: 
    print('Some error occur')
