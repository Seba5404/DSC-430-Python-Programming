#Sebastian Zdarowski
#I have not given or received any unauthorized assistance on this assignment.”  
#Sept 24th, 2018


def game():
    'run game function, user input required' #doc string
    over = False 
    print("Starting Word:STAR")
    count = 0
    wordC = ["S","T","A","R"]
    while not over:
        print("Current placement is " + str(wordC)) #current placement of word
        print("Option 1: Remove a character.")
        print("Option 2: Insert a character.")
        print("Option 3: Replace a character. ")
        choice = input("What would you like to do please enter in 1, 2 or 3: ")
        

        if int(choice) == 1: #remove character
            choice1 = input("Where character would you like to remove?: ")
            wordC.remove(choice1.upper()) #remove character from the list 
            count += 1
        if int(choice) == 2: #replace character
            choice2 = input("What Character would you like to insert? ")
            choice2placement = input("Where would you like to insert the character index wise? ")
            wordC.insert(int(choice2placement),choice2.upper()) #allow user to insert a new character wherever they like
            print(wordC)
            count += 1
        if int(choice) == 3: # allow user to replace a letter with another 
            choice3 = input("What Character would you like to replace?: ")
            choice3Val = input("What would you like to put in its place?: ")
            placement = wordC.index(choice3.upper())
            wordC.remove(choice3.upper()) #remove old value
            wordC.insert(placement,choice3Val.upper()) #insert new value
            count += 1
        
        fullWord = "" #blank value always blank out and check if user has correct word
        checkWord = wordC

        checkWord.reverse() #reverse order of the words so itll print out correctly
        for x in checkWord:
            fullWord = x + fullWord
        
        
        if fullWord.upper() == "GOAL":
            over = True
        wordC.reverse() #change word back correctly
    return count


username = input("Hello what is your name?: ")
print("Play my game, your starting word is STAR, you'll have the choice to enter in words at any index point")
#Word to get in this game is GOAL
count = game() #main code for program 
print(str(username) +" it took you "+ str(count)+ " steps to guess the word!")
        
