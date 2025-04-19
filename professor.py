import random

levelList = [1,2,3]
level = int(input('Please enter a level up to 3: ')) # What's the point of the level?
prob = 1
score = 0
tries = 3 # Level?

def levelChecker(level, levelList):
    if level not in levelList:
        return 'False'
    else:
        return 'True'
    
while levelChecker(level, levelList) == 'False':
    print('Please enter 1-3')
    level = int(input('Please enter a level up to 3: '))
    levelChecker(level, levelList)

while prob <= 10:
    first = random.randint(0,10)
    second = random.randint(0,10)
    probFormat = (f'{first} + {second} = ')
    answer = int(input(probFormat))

    if answer == first + second:
        score +=1
    else:
        while answer != first + second:
            print('EEE')
            # print(tries)
            tries -=1
            if tries == 0:
                print(f'{probFormat} {first + second}')
                break
            answer = int(input(probFormat))
            if answer == first + second:
                score += 1

    #print(f'{score}\n')
    prob += 1

print(f'Score: {score}')