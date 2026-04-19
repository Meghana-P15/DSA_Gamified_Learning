import time
replay= True
while replay:
 print("\n🧠Mind Reading Game")
 print("Instructions:")
 print("Think of a nunber within the range you choose")
 print("I will try to guess it, and tell me if the number is Higher(H) or Lower(L) or Correct(yes)\n") ")
 try:
   initial=int(input("Set the initial value for the guess"))
   stop=int(input("Set the stop value for the guess"))
 except ValueError:
     print("Please enter valid numbers!")
     continue
 if initial>=stop:
     print("Start must be less than stop!")
     continue
 print(f"\n Current range:{initial} to {stop}")

 guess="no"
 attempts=0
 while(guess.lower()!="yes"):
  if initial>stop:
     print("🤔 Something doesn't add up. Did you change the number?")
     break
  attempts+=1
  number=(initial+stop)//2
  for i in range(3):
    print("Thinking"+"."*(i+1))
    time.sleep(0.4)
  print(f"My guess is {number}")
  guess=input("Type yes/Yes if the guess is correct otherwise type No/no")
  if(guess.lower()=="yes"):
    print("🎉Got it!I guessed your number🎉")
    print(f"It took me {attempts} attempt(s)")
    break

  else:
     x=input("Type H/h if the number is higher than the guessed number and type L/l if the number is less than the guessed number")
     if(x.lower()=='h'):
         initial=number+1
     elif(x.lower()=='l'):
         stop=number-1
     else:
         print("❌Invalid input! Please type H or L")
         continue
     print(f"📉 Updated range:{initial} to {stop}")
  choice=input("\nDo you want to re[lay? (y/n):")
  if( choice.lower !='y':
      replay=False
print("\n👋 Thanks for playing")
    
