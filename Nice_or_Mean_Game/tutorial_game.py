##Python 3.11.7
##
##Author: Spencer Mason
##
##Text-based game tutorial

def start(nice = 0, mean = 0, name = ""):
    #get users name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    """
        Check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    #meaning, if we do not already have this user's name,
    #Then they are a new player and we need to get their name
    if name != "":
        print("\nHere we go again, {}...".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nPlease enter your name. \n>>> ").capitalize()
                if name != "":
                    print("\nHello, {}.".format(name))
                    print("\nWelcome to my super-complex \nchoose-your-own-story game. You will be \ngreeted by multiple colorful characters,")
                    print("and decide how you interact with them. \nYour fate will be determined by your actions")
                    stop = False
    return name

def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger takes advantage \nof your ignorance and mugs you...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger shuffles away, muttering under their breath: \n'You'll get what's coming to you...'")
            mean = (mean + 1)
            stop = False
    score(nice, mean, name) #Pass the 3 variables to the score()

def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))

def score(nice, mean, name):
    #Score function is being passed the values stored within the 3 variables
    if nice > 2: #If condition is valid, call win function passing in the variables so it can use them
        win(nice, mean, name)
    if mean > 2: #If condition is valid, call lose function passing in the variables so it can use them
        lose(nice, mean, name)
    else: #Else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    #Substitute the {} wildcards with our variable values
    print("\nWell, {}, you're beat up and broke,\nbut at least you have decent morals and\ndidn't compromise them.".format(name))
    #Call again function and pass in our variables
    again(nice, mean, name)

def lose(nice, mean, name):
    #Substitute the {} wildcards with our variable values
    print("\nSo, {}, you were pretty rude. But they deserved it.\nTrust me, those people were going to mug you.".format(name))
    #Call again function and pass in our variables
    again(nice, mean, name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice, mean, name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user has elected to play again
    start(nice, mean, name)





if __name__ == "__main__":
    start()
