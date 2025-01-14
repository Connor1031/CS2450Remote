#age guesser
import random
def ageGuess():
    realage = False
    notage = []
    print("Hello, I am going to guess your age.\nWhat is your name?")
    name = input()
    while not realage:
        ages = random.randrange(15, 30)
        if ages in notage:
            continue
        print("Is your age " + str(ages) +"? \nType Y or N.")
        yesorno = input().strip().upper()
        if yesorno == 'Y':
            realage = ages
            break
        elif yesorno == 'N':
            notage.append(ages)
            print("Rats.")
        else:
             print('Input not recognised. Type Y or N next time.')
    print(f"{name} is {realage} years old.")
ageGuess()