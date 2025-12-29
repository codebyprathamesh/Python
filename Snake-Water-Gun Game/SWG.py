import random
point=0
j=1
opponent=0
game=["S","W","G"]

print("-----------------SNAKE WATER GUN GAME-------------------\n")
while j<6:
    print(f"Round {j}")
    output= random.choice (game)
    user_choice=input(" Snake(S),Water(W),Gun(G)\n Enter your Choice :")
    if((user_choice.upper()=='S' and output.upper()=='W') or (user_choice.upper()=='W' and output.upper()=='G') or user_choice.upper()=='G' and output.upper()=='S' ):
        print("Opponents Choice:",output,"\n")
        point+=1
        j+=1
        print(f"Your Score: {point} point(s)\n Opponents Score:{opponent}\n")
        continue
    elif ((user_choice.upper()=='W' and output.upper()=='S') or (user_choice.upper()=='G' and output.upper()=='W') or user_choice.upper()=='S' and output.upper()=='G') :
        print("Opponents Choice:",output,"\n")
        
        j+=1
        opponent+=1 
       
        print(f"Your Score: {point} point(s)\n Opponents Score:{opponent}\n")
        continue
    if user_choice.upper() not in ['S','W','G']:

        raise TypeError
    else:continue

if(opponent==point and j==6):
     print("MATCH TIED!! \n")
     print("GAME  OVER \n")
    
if(opponent>point):
        print("You Lose!!\nBetter Luck Next Time...")
        
if(opponent<point):
        print("You Won!!\n")
        

