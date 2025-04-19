import random

def number():
    def game():
        number = random.randint(1,10)
        guess = int(input('Guess 1-10: '))

        if guess == number:
            print('You Win!')

        while guess != number:
            if number > guess:
                print('Too low :(')
                guess = int(input('Guess 1 - 10: '))
            else:
                print('Too high')
                guess = int(input('Guess 1-10: '))

            if guess == number:
                print('You Win!')

    game()

def star():
    direction = input('Would you like it descending or ascending: ').lower()
    row = int(input('How many rows would you like: '))
    currentrow = 1

    if direction == 'ascending':
        while currentrow <= row:
            print('*' * currentrow)
            currentrow += 1
    else:
        while currentrow <= row:
            print('*' * row)
            row -= 1

##################SHOULD HAVE MADE THIS A DIFFERENT FILE####################
which = input('Number or stars: ')
if which == 'stars':
    star()
else:
    number()