import random 
number=random.randint(1,200)
count=0
print('''------PERFECT GUESS GAME 🧠🤓------\n''')
start=int(input('''PRESS 1 to PLAY
                   PRESS 2 TO KNOW ABOUT THE GAME'''))
def help():
     """
    This is a number guessing game.
    It counts wrong attempts and gives feedback
    based on the number of attempts.
    """
while(True):   
    if(start==2):
        print(help.__doc__)
        d=str(input('''Press P to play Press Q to quit'''))
        
        if(d=="P"):
            start=1
            break
        elif (d=="Q"):
            print("___GAME OVER___")
            break
    elif(start==1):
        break
    else:
            try:raise ValueError
            except:
                print("Please input a valid operation or press Q to quit.\n") 
                continue
def Guess_Number():
    print("-----🏁GAME STARTED🏁-----")
    while(True and start==1):
        guess=int(input('''
                        Guess a number from 1 to 200\n'''
                        ))
        if(guess==number):
            print(f'''                   Congratulations😁🎊
                You've Guessed the correct number in {count} wrong attempt(s)!\n''')
            if(count==0):
                print("You are insane guesser bro😉\n")
                break
            elif(count>0 and count<=5):
                print("Well Played Bro👌\n")
                break
            elif(count>5 and count<10):
                print("Good Try in Guessing the number😊/n")
                break
            elif(count>10):
                print("Good Try bro. Can do better!")
                break

                
            break
        elif(guess>number):
            print(f'''Oops!
                The Number You've Guessed is Greater than the number.
                Please try another guess, or press 0 to end the game\n''')
            count+=1 
            continue
            
            
        elif(guess<number):
            print('''Oops!
                The Number You've Guessed is less than the number.
                Please try another guess, or press 0 to end the game\n''')
            count+=1
            continue
        elif(guess==0):
                print("----------GAME OVER-----------")
                break
        else:
            try :
                raise ValueError 
            except:
                print("Please Enter the Number between 1 and 200")
                continue
        
                

