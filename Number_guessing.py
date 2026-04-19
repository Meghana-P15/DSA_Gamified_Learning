#Number Guessing

import random

print("Hello! This is a random number guessing game")

choice="y"
BestScore=[]
#It will generate a random number between the range(both included)
def play_game(start,stop,max_attempts):
    number=random.randint(start,stop)
    attempts=0
    win=false

while choice=="y" or choice=="Y":
 print("Enter your level")
 print("1. Easy-->Guess the number between 1 to 50 and only 15 attempts are allowed")
 print("2. Medium-->Guess the number between 1 to 100 and only 10 attempts are allowed")
 print("3. Hard-->Guess the number between 1 to 100 and only 5 attempts are allowed")
 print("4. Customizable-->You are allowed to customize your game")

 try:
     level=int(input()
 except ValueError:
     print("Enter a valid number!")
     continue
    
 num=0
 attempts=0
 win=False
 match level:
    case 1:
        #It will generate a random number between 1 to 100 (Both are included)
        
        while num!=number and attempts<15:
         
         try:
             num=int(input("Guess the number:"))
         except ValueError:
             print("Enter a valid number!")
             continue
         if(num<1 or num>50):
             print("Enter number between 1 and 50")
             continue
         attempts+=1
         if(num==number):
            print("You won!")
            win=True
            break
         elif(num<number+2 and num>number-2):
            print("Almost there! One more nudge!")
         elif(num<number+5 and num>number-5):
            print("So close! 👀,guess quickly!!")
         elif(num<number+10 and num>number-10):
            print("Somewhere near to the number, try a little harder next time!")
         elif(num<number-10):
            print("Guess Higher Number, you’re way off 🔥🔥")
         elif(num>number+10):
            print("Guess Lower Number, you’re way off 🔥🔥")     

          print("Total number of attempts:",attempts)
        if(win):
           BestScore.append(attempts)
        else:
            print("Better luck next time, Don't lose your confidence!")
            print("Actual Number is ",number)
        
    case 2:
    #It will generate a random number between 1 to 100 (Both are included)
        number=random.randint(1,100)
        while num!=number and attempts<10:
          attempts+=1
          num=int(input("Guess the number:"))
          if(num<1 or num>100):
             print("Enter number between 1 and 100")
             attempts-=1
             continue
          else:
           if(num==number):
             print("You won!")
             win=True
             break
           elif(num<number+2 and num>number-2):
             print("Almost there! One more nudge!")
           elif(num<number+5 and num>number-5):
             print("So close! 👀,guess quickly!!")
           elif(num<number+10 and num>number-10):
             print("Somewhere near to the number, try a little harder next time!")
           elif(num<number-10):
             print("Guess Higher Number, you’re way off 🔥🔥")
           elif(num>number+10):
             print("Guess Lower Number, you’re way off 🔥🔥")     

           if(win):
            BestScore.append(attempts)
           else:
            print("Better luck next time, Don't lose your confidence!")
            print("Actual Number is ",number)

    case 3:
        #It will generate a random number between 1 to 100 (Both are included)
        number=random.randint(1,100)
        while num!=number and attempts<5:
          attempts+=1
          num=int(input("Guess the number:"))
          if(num<1 or num>100):
             print("Enter number between 1 and 100")
             attempts-=1
             continue
          else:
           if(num==number):
             print("You won!")
             win=True
             break
           elif(num<number+2 and num>number-2):
             print("Almost there! One more nudge!")
           elif(num<number+5 and num>number-5):
             print("So close! 👀,guess quickly!!")
           elif(num<number+10 and num>number-10):
             print("Somewhere near to the number, try a little harder next time!")
           elif(num<number-10):
             print("Guess Higher Number, you’re way off 🔥🔥")
           elif(num>number+10):
             print("Guess Lower Number, you’re way off 🔥🔥")     

        if(win):
          BestScore.append(attempts)
        else:
          print("Better luck next time, Don't lose your confidence!")
          print("Actual Number is ",number)

    case 4:
        #It will generate a random number between 1 to 100 (Both are included)
        start=int(input("Enter the start value for the game:"))
        stop=int(input("Enter the stop value for the game:"))
        customAttempt=int(input("Enter the number of attempts to challenge yourself:"))
        attempts=1
        number=random.randint(start,stop)
        while num!=number and attempts<customAttempt:
         attempts+=1
         num=int(input("Guess the number:"))
         if(num<start or num>stop):
             print("Enter number between ",start," and ",stop)
             attempts-=1
             continue
         else:
          if(num==number):
            print("You won!")
            win=True
            break
          elif(num<number+2 and num>number-2):
            print("Almost there! One more nudge!")
          elif(num<number+5 and num>number-5):
            print("So close! 👀,guess quickly!!")
          elif(num<number+10 and num>number-10):
            print("Somewhere near to the number, try a little harder next time!")
          elif(num<number-10):
            print("Guess Higher Number, you’re way off 🔥🔥")
          elif(num>number+10):
            print("Guess Lower Number, you’re way off 🔥🔥")     

        if(win):
          BestScore.append(attempts)
        else:
          print("Better luck next time, Don't lose your confidence!")
          print("Actual Number is ",number)

    case _:
        print("Enter the number between 1 to 4!")
 print("To continue the game, enter y/Y")
 choice=input()
 if (choice!="y" and choice!="Y"):
     print("Your Best attempt: ",min(BestScore))


