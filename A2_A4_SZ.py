#Sebastian Zdarowski 
#I have not given or received any unauthorized assistance on this assignment
#OCT 8th, 2018
import random
done = False


def game(accBal,choice): #function to calculate chances of game 
    'Function that runs the game, inputs accbalance and the user input'
    die = int(random.randint(1,6)) #set up die 1
    die2 = int(random.randint(1,6)) #set up die 2
    die3 = int(random.randint(1,6)) #set up die 3
    
    print("Dice one roll is " + str(die))
    print("Dice two roll is " + str(die2))

    dieSum = die + die2 # add up sum of die

    if dieSum == 7 or dieSum == 12:
        betValue = float(choice) * 2 #double value of the bet WINNER!!
        print("You are a winner!")
        print("You have won $"+ str(betValue))
    else:
        thirdTry = input('What you like to double your bet and roll a third die? Yes or No: ')
        if thirdTry.upper() == "YES":
            diesum2 = die + die2 + die3
            if diesum2 == 7 or diesum2 == 12:
                newChoice = float(choice) * 2 #double the bet
                betValue = float(newChoice)*3 #times 3 her double bet 
                print("You are a winner!")
                print("You have won $"+ str(betValue))
            else:
                betValue = (float(choice) * 2) * -1 #lose money 
                print("You have lost $"+ str(round(float(choice) *2,2)))
        elif thirdTry.upper() == "NO":
            betValue = float(choice) * -1
            print("You have lost $" +str(round(float(choice),2)))

    newBalance = accBal + betValue
    #print(newBalance)
    return newBalance


def labMenu():
    'Menu Selection screen' #docstring
    print('Enter a bet.')
    print('Press Enter if you are done. ')
    
accBal = 100 #Starting account balance 

while not done:
    labMenu()
    
    if accBal <= 0: #once user runs out of money, close out game
        print("You are out of money, game is over. Thanks for playing!")
        print("Your final Account Balance is " + str(round(float(accBal),2)))
        done = True #set up as true, exit game 
        break #leave the game user is out of money 
    
    try:
        print("Your current Account Balance is $" + str(round(float(accBal),2)))
        choice = input('Please make an entry: ')
        if choice == '':
            done = True
            print("Your total Account Balance is $"+ str(round(float(accBal),2)))
            break #enter, error catch works in idle/ leave game 

        if float(choice) < 0:
            print("Please enter a value higher than 0.")#incase user enters in a negative value 
    except ValueError: #catch error if user presses enter by mistake or not an integer
            print("Please enter a valid number in float format 00.00")
            choice = input('Please make an entry: ') #give user another try

    if float(choice) > 0: #if its a valid bet go to game 
        if float(choice) <= float(accBal):
            newBalance = game(accBal,choice) #call function for game
            accBal = newBalance #set up new value
        # print(accBal)
        else:
            print("You cant bet higher than your account balance, try again.")
    
