#age guesser
import random
def ageGuess():
    realage == False
    notage = []
    print("Hello, I am going to guess your age.\nWhat is your name?")
    name = input()
    while realage == False:
        ages = random.randrange(15, 30)
        if ages in notage:
            return
        print("Is your age " + ages +"? \nType Y or N.")
        yesorno = input()
        if yesorno == Y or y:
            realage = ages
        elif yesorno == N or n:
            notage.append(ages)
            print("Rats.")
        else:
             print('Input not recognised. Type Y or N.')
    print(name + "is " + realage + 'years old')
        